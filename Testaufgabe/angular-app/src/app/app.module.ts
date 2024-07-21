import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }  from './app.component';
import { HttpClient } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';  // Wichtig für Angular Material
import { MatTableModule, MatTableDataSource } from '@angular/material/table';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule, MatSort } from '@angular/material/sort';


@NgModule({
  imports: [ 
    BrowserModule,
    BrowserAnimationsModule,  // Wichtig für Angular Material
    MatTableModule,
    MatSortModule,
    MatSort,
    MatPaginatorModule,
    MatTableDataSource,
    MatPaginator,
    HttpClient,
    ],
  declarations: [ AppComponent ],
  bootstrap:    [ AppComponent ]
})

export class AppModule { }
