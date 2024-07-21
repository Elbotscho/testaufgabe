import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { VersichertenDatenComponent } from './versichertendaten/versichertendaten.component';
import { VersicherungsvertraegeComponent } from './versicherungsvertraege/versicherungsvertraege.component';
import { SchadensfaelleComponent } from './schadensfaelle/schadensfaelle.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet, 
    RouterLink, 
    VersichertenDatenComponent, 
    VersicherungsvertraegeComponent, 
    MatToolbarModule, 
    MatButtonModule, 
    SchadensfaelleComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'angular-app';
}
