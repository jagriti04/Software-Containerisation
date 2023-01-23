import { Component, Input } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { QuestionModel } from './QuestionModel';

@Component({
  selector: 'app-add-survey',
  templateUrl: './add-survey.component.html',
  styleUrls: ['./add-survey.component.css']
})
export class AddSurveyComponent {
  @Input() question!: QuestionModel<string>;
  @Input() form!: FormGroup;
  get isValid() { return this.form.controls[this.question.key].valid; 
  }
  
}
