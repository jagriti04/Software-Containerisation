import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddSurveyComponent } from './add-survey/add-survey.component';
import { AppComponent } from './app.component';
import { TakeSurveyComponent } from './take-survey/take-survey.component';

const routes: Routes = [
  { path: 'add-survey', component: AddSurveyComponent },
  { path: 'survey', component: TakeSurveyComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
  
}