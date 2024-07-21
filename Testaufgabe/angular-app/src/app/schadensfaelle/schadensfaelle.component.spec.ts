import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SchadensfaelleComponent } from './schadensfaelle.component';

describe('SchadensfaelleComponent', () => {
  let component: SchadensfaelleComponent;
  let fixture: ComponentFixture<SchadensfaelleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SchadensfaelleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SchadensfaelleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
