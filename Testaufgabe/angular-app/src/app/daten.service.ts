import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DatenService {

  private apiUrl = '${environment.apiUrl}/'; // URL zu deinem FastAPI-Endpunkt

  constructor(private http: HttpClient) { }

  get_versichertendaten(page: number, size: number): Observable<any[]> {
    return this.http.get<any>(this.apiUrl + `versichertendaten?page=${page}&size=${size}`);
  }

  get_versicherungsvertreage(page: number, size: number): Observable<any[]> {
    return this.http.get<any>(this.apiUrl + `versicherungsvertraege?page=${page}&size=${size}`);
  }

  get_schadensfaelle(page: number, size: number): Observable<any[]> {
    return this.http.get<any>(this.apiUrl + `schadensfaelle?page=${page}&size=${size}`);
  }

  downloadCsv(app: string, page: number, size: number): Observable<Blob> {
    return this.http.get(this.apiUrl + `download-csv?app=${app}&page=${page}&size=${size}`, { responseType: 'blob' });
  }

}
