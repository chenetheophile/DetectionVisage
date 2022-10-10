import { Component, OnInit } from '@angular/core';
import { FaceStudent } from './models/face-students.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  myFace!: FaceStudent;
  myOtherFace1!: FaceStudent;
  myOtherFace2!: FaceStudent;
  myOtherFace3!: FaceStudent;

  ngOnInit() {
    this.myFace = new FaceStudent(
      'Théophile Chêne',
      'Chef de projet',
      './assets/Images/inconnu.webp',
      new Date(),
      0
    );
    this.myOtherFace1 = new FaceStudent(
      'Adrien Tirlemont',
      'Expert en IA',
      './assets/Images/inconnu.webp',
      new Date(),
      0
    );
    this.myOtherFace2 = new FaceStudent(
      'Clément Cronier',
      'Web designer',
      './assets/Images/inconnu.webp',
      new Date(),
      0
    );
    this.myOtherFace3 = new FaceStudent(
      'Autre',
      'Utilisateur',
      './assets/Images/inconnu.webp',
      new Date(),
      0
    );
  }
}
