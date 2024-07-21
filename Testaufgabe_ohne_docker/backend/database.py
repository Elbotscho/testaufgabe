from sqlalchemy import create_engine, Column, String, Date, ForeignKey, Float, Enum, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# SQLite-Datenbank erstellen
engine = create_engine('sqlite:///db/versicherung.db', connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Versichertendaten(Base):
    __tablename__ = 'versichertendaten'

    versichertennummer = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    geburtsdatum = Column(Date, nullable=False)
    adresse = Column(String(255), nullable=False)

    vertraege = relationship('Versicherungsvertrag', back_populates='versichertendaten')

class Versicherungsvertrag(Base):
    __tablename__ = 'versicherungsvertraege'

    vertragsnummer = Column(String(36), primary_key=True)
    versichertennummer = Column(String(36), ForeignKey('versichertendaten.versichertennummer'), nullable=False)
    vertragsbeginn = Column(Date, nullable=False)
    vertragsende = Column(Date)
    vertragsstatus = Column(Enum('aktiv', 'gekündigt', 'abgelaufen'), nullable=False)

    versichertendaten = relationship('Versichertendaten', back_populates='vertraege')
    schadensfaelle = relationship('Schadensfall', back_populates='versicherungsvertrag')

class Schadensfall(Base):
    __tablename__ = 'schadensfaelle'

    schadensnummer = Column(String(36), primary_key=True)
    vertragsnummer = Column(String(36), ForeignKey('versicherungsvertraege.vertragsnummer'), nullable=False)
    datum = Column(Date, nullable=False)
    schadenstyp = Column(Enum('Unfall', 'Diebstahl', 'Feuer'), nullable=False)
    schadenhoehe = Column(Float, nullable=False)

    versicherungsvertrag = relationship('Versicherungsvertrag', back_populates='schadensfaelle')

class ExportLog(Base):
    __tablename__ = 'export_log'

    id = Column(Integer, primary_key=True, index=True)
    tabellenname = Column(String, index=True)
    exportanzahl = Column(Integer)
    zeitstempel = Column(DateTime, default=datetime.now())


# Erstelle die Tabellen in der Datenbank
Base.metadata.create_all(engine)


