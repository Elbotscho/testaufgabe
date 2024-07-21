import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VersicherungsvertraegeComponent } from './versicherungsvertraege.component';

describe('VersicherungsvertraegeComponent', () => {
  let component: VersicherungsvertraegeComponent;
  let fixture: ComponentFixture<VersicherungsvertraegeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VersicherungsvertraegeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VersicherungsvertraegeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
