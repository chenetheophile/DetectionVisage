import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FaceStudentsComponent } from './face-students/face-students.component';

@NgModule({
  declarations: [
    AppComponent,
    FaceStudentsComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
