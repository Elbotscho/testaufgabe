import { Component, OnInit } from '@angular/core';
import { DatenService } from '../daten.service';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-versicherungsvertraege',
  standalone: true,
  imports: [MatTableModule, MatPaginatorModule, MatFormFieldModule, FormsModule, MatButtonModule],
  templateUrl: './versicherungsvertraege.component.html',
  styleUrl: './versicherungsvertraege.component.css'
})
export class VersicherungsvertraegeComponent implements OnInit {
  displayedColumns: string[] = ['vertragsnummer', 'versichertennummer', 'vertragsbeginn', 'vertragsende', 'vertragsstatus'];
  dataSource = new MatTableDataSource<any>();
  
  totalItems = 0;
  pageSize = 10;
  pageIndex = 0;
  pageSizeOptions = [10, 25, 50]

  constructor(private datenService: DatenService) { }

  ngOnInit() {
    this.loadData(this.pageIndex + 1, this.pageSize);
  }

  loadData(page: number, size: number) {
    this.datenService.get_versicherungsvertreage(page, size).subscribe((response:any) => {
      this.dataSource.data = response.items;
      this.totalItems = response.totalItems;
      this.pageSizeOptions = [10, 25, 50, response.totalItems];
    });
  }

  onPageChange(event: PageEvent) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.loadData(this.pageIndex + 1, this.pageSize);
  }

  downloadCsv() {
    this.datenService.downloadCsv('versicherungsvertraege', this.pageIndex, this.pageSize).subscribe((response: Blob) => {
      const url = window.URL.createObjectURL(response);
      const a = document.createElement('a');
      console.log(response);
      a.href = url;
      const filename = 'versicherungsvertraege_' + (this.pageIndex * this.pageSize + 1) + '_' + (this.pageIndex * this.pageSize + this.pageSize) + '.csv';
      a.download = filename; 
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    });
  }
}

