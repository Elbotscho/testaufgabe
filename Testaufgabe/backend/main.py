from fastapi import FastAPI, Depends, Request, Query, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from typing import Optional
from datetime import date
import csv
import io

from database import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ermögliche Anfragen von allen Ursprüngen
    allow_credentials=True,
    allow_methods=["*"],  # Ermögliche alle Methoden (GET, POST, etc.)
    allow_headers=["*"],  # Ermögliche alle Header
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/versichertendaten")
async def get_versichertendaten(page: int = Query(1, gt=0), size: int = Query(10, gt=0), db: Session = Depends(get_db)):
    start = (page - 1) * size
    end = start + size

    versichertendaten = db.query(Versichertendaten).all()
    paginated_items = versichertendaten[start:end]

    for item in paginated_items:
        item.geburtsdatum = format_date(item.geburtsdatum)

    return {"items": paginated_items, "totalItems": len(versichertendaten)}


@app.get("/versicherungsvertraege")
async def get_versicherungsvertraege(page: int = Query(1, gt=0), size: int = Query(10, gt=0), db: Session = Depends(get_db)):
    start = (page - 1) * size
    end = start + size

    versicherungsvertraege = db.query(Versicherungsvertrag).all()
    paginated_items = versicherungsvertraege[start:end]
    
    for item in paginated_items:
        item.vertragsbeginn = format_date(item.vertragsbeginn)
        if item.vertragsende == None:
            item.vertragsende = "unbefristet"
        else:
            item.vertragsende = format_date(item.vertragsende)

    return {"items": paginated_items, "totalItems": len(versicherungsvertraege)}


@app.get("/schadensfaelle")
async def get_versicherungsvertraege(page: int = Query(1, gt=0), size: int = Query(10, gt=0), db: Session = Depends(get_db)):
    start = (page - 1) * size
    end = start + size

    schadensfaelle = db.query(Schadensfall).all()
    paginated_items = schadensfaelle[start:end]

    for item in paginated_items:
        item.datum = format_date(item.datum)
    
    return {"items": paginated_items, "totalItems": len(schadensfaelle)}


@app.get("/download-csv")
async def download_csv(app: str, page: int, size: int, db: Session = Depends(get_db)):
    model = get_model(app)
    csv_data = db.query(model).all()

    start = page * size
    end = start + size
    csv_data = csv_data[start:end]

    output = io.StringIO()
    writer = csv.writer(output)
    
    # Dynamisch die Spaltennamen abfragen
    columns = [column.key for column in inspect(model).columns]
    writer.writerow(columns)  # Kopfzeile der CSV

    for row in csv_data:
        writer.writerow([getattr(row, column) for column in columns])

    log_download(db, app, size)

    response = Response(content=output.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=file.csv"
    return response

def get_model(app):
    model_map = {
        "versichertendaten": Versichertendaten,
        "versicherungsvertraege": Versicherungsvertrag,
        "schadensfaelle": Schadensfall
    }
    
    model = model_map.get(app)
    if not model:
        raise HTTPException(status_code=400, detail="Invalid table name")
    return model

def log_download(db, app, size):
    export_log = ExportLog(
        tabellenname=app,
        exportanzahl=size,
    )
    db.add(export_log)
    db.commit()

def format_date(d: Optional[date]) -> str:
    return d.strftime("%d.%m.%Y")