import { Routes } from '@angular/router';
import { VersichertenDatenComponent } from './versichertendaten/versichertendaten.component';
import { VersicherungsvertraegeComponent } from './versicherungsvertraege/versicherungsvertraege.component';
import { SchadensfaelleComponent } from './schadensfaelle/schadensfaelle.component';

export const routes: Routes = [
    { path: 'versichertendaten', component: VersichertenDatenComponent },
    { path: 'versicherungsvertraege', component: VersicherungsvertraegeComponent },
    { path: 'schadensfaelle', component: SchadensfaelleComponent },
];

