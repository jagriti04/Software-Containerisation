import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import{ Constants } from './config/constants';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private https: HttpClient) { 
  }

  rootURL = Constants.API_ENDPOINT;

  getUsers() {
    return this.https.get(this.rootURL + 'survey/all-users');
  }

  addUser(user: any) {
    return this.https.post(this.rootURL + 'survey/add-user/', { user});
  }

}
