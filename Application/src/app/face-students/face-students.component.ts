import { Component, OnInit, Input } from '@angular/core';
import { FaceStudent } from '../models/face-students.model';

@Component({
  selector: 'app-face-students',
  templateUrl: './face-students.component.html',
  styleUrls: ['./face-students.component.scss']
})

export class FaceStudentsComponent implements OnInit {
  @Input() faceStudent!: FaceStudent;
  textButton!: string;

  ngOnInit() {
    this.textButton ='Like';
  }
  onSnap() {
    if (this.textButton == 'Like') {
      this.faceStudent.snaps++;
      this.textButton = 'Liked it'
    }
    else if(this.textButton == 'Liked it') {
      this.textButton='Like';
      this.faceStudent.snaps--;
    }
  }
}
