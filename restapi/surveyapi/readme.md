First run the requirement.txt, using following command
$ pip install -r requirement.txt

To run the project at localhost/ http://127.0.0.1:8000 (default port is 8000)
$ python manage.py runserver

To create superuser, need following command and access admin UI (to modify database) at http://127.0.0.1:8000/admin/ 
$ python manage.py createsuperuser 

Queries can also executed at Python Shell using:
$ python manage.py shell
Example query: 
>> from surveyapi.models import SurveyUser
>> user = SurveyUser.objects.create(name="test", username="qwery123")      #to add new object
>> user.save()                      #save object in database

API endpoints:
1. '/survey/<int:survey_version>/', Method = GET, description = to fetch details of survey by providing it's version
2. '/survey/all-users', Method = GET, description = to fetch all usernames
3. '/survey/add-user/', Method = POST, description = to add a user, it needs a requestbody

For this project MySQL database is used.
Database details are present in survey/settings.py file and to use the default sqlite db uncomment lines 79-82 and comment 83-91,

Details of models are present in surveyapi/models.py file

APIs were tested using Postman, screenshots - add-user.png, all-users.png and survey-version.png