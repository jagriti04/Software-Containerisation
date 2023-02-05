import { Injectable } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { QuestionModel } from './add-survey/QuestionModel';

@Injectable({
  providedIn: 'root'
})
export class SurveyService {
  
  toFormGroup(questions: QuestionModel<string>[] ) {
    const group: any = {};

    questions.forEach(question => {
      group[question.key] = question.required ? new FormControl(question.value || '', Validators.required)
                                              : new FormControl(question.value || '');
    });
    return new FormGroup(group);
  }

  constructor() { }
}
