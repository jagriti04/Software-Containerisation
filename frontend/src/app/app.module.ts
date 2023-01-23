import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SurveyCompComponent } from './survey-comp/survey-comp.component';
import { HttpClientModule } from '@angular/common/http';
import { UserDetailsComponent } from './user-details/user-details.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AddSurveyComponent } from './add-survey/add-survey.component';
import { TakeSurveyComponent } from './take-survey/take-survey.component';


@NgModule({
  declarations: [
    AppComponent,
    SurveyCompComponent,
    UserDetailsComponent,
    AddSurveyComponent,
    TakeSurveyComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
