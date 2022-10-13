import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { FaceStudentsComponent } from './face-students/face-students.component';
import { PdfViewerComponent } from './pdf-viewer/pdf-viewer.component';
import { PdfViewerModule } from 'ng2-pdf-viewer';

@NgModule({
  declarations: [
    AppComponent,
    FaceStudentsComponent,
    PdfViewerComponent,
  ],
  imports: [
    BrowserModule, PdfViewerModule,
    RouterModule.forRoot([
      { path: 'Notreprojet', component: PdfViewerComponent },
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
