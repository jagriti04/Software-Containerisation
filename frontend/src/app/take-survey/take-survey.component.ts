import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Subject, takeUntil } from 'rxjs';
import { AppService } from '../app.service';

@Component({
  selector: 'app-take-survey',
  templateUrl: './take-survey.component.html',
  styleUrls: ['./take-survey.component.css']
})
export class TakeSurveyComponent {

  constructor(private appService: AppService) {}

  userForm = new FormGroup({
    name: new FormControl(''),
    userName: new FormControl('')
  });


  users: any[] = [];
  userCount = 0;

  destroy$: Subject<boolean> = new Subject<boolean>();

  onSubmit() {

    this.appService.addUser(this.userForm.value).pipe(takeUntil(this.destroy$)).subscribe(data => {
      console.log('message::::', data);
      this.userCount = this.userCount + 1;
      console.log(this.userCount);
      this.userForm.reset();
    });
  }
  
  getAllUsers() {
    this.appService.getUsers().pipe(takeUntil(this.destroy$)).subscribe((data: any) => {
        this.users = data.users;
        console.log(this.users);
    });
  }

  ngOnDestroy() {
    this.destroy$.next(true);
    this.destroy$.unsubscribe();
  }
}
