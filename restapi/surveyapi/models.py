from django.db import models

# Create your models here.
# to save details of survey
class Survey(models.Model):
    s_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    survey_version = models.IntegerField(default=0, blank=False, unique=True)
    number_of_questions = models.IntegerField(default=0, blank=False)
    description = models.TextField(default="")
    def __str__(self):
        return str(self.survey_version)

# to save details of questions 
class Questions(models.Model):
    MCQ = 'MCQ'
    TEXT = 'TEXT'
    TYPE_CHOICES = [
        (MCQ, 'Multiple Choice Questions'),
        (TEXT, 'Long text'),
    ]
    q_id = models.AutoField(primary_key=True)
    question_text = models.TextField(blank=False)
    question_type = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
        default=MCQ,)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return str(self.question_text)

# to store details choices along with questions
class Choices(models.Model):
    c_id = models.AutoField(primary_key=True)
    choice_text = models.CharField(max_length=150, blank=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, default="")
    def __str__(self):
        return str(self.choice_text)


# table to store user information
class SurveyUser(models.Model):
    u_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.username)

# To store user response, questions and answer
class UserResponse(models.Model):
    ur_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE, default="")
    created_date = models.DateTimeField(auto_now=True)
    survey = models.ManyToManyField(Survey, blank=False)
    user_response_text = models.ForeignKey(Choices, on_delete=models.CASCADE, related_name='user_response', default='')
    def __str__(self):
        return str(self.ur_id)

# 
#  migrations.DeleteModel('Choices'),
#         migrations.DeleteModel('Questions'),
#         migrations.DeleteModel('Survey'),
#         migrations.DeleteModel('SurveyUser'),
#         migrations.DeleteModel('UserResponse'),
