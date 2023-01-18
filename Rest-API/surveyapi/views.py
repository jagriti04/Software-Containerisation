import json
from django.shortcuts import render
from django.core import serializers

from .models import SurveyUser, Survey, Questions, Choices, UserResponse


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.conf import settings

# Create your views here.

@csrf_exempt
@api_view(["GET"])
def homePageView(request):
    response = {"status": "Hello world", "message": "no rows found"}
    return HttpResponse(
        json.dumps(response), content_type="application/json", status=200
    )

@csrf_exempt
@api_view(["GET"])
def users_list(request):
    # """
    # Gets a list of all users.
    # """
    all_users = SurveyUser.objects.all().values_list("username", flat=True)     #fetch users and return usernames

    if len(all_users) > 0:
        keys = [str(x) for x in all_users]
        response = {"status": "success", "username": keys}
    else:
        response = {"status": "error", "message": "no rows found"}
    return HttpResponse(
        json.dumps(response), content_type="application/json", status=200
    )

@csrf_exempt
@api_view(["GET"])
def survey_by_version(request, survey_version):
    # """
    # Gets a survey questionairre by survey version.
    # """
    survey_exists = Survey.objects.filter(survey_version=survey_version).exists()   #to check if survey exists or not

    if survey_exists:
        survey = list(Survey.objects.filter(survey_version=survey_version).values_list("survey_name", "survey_version", "questions"))
        response = {"status": "success", "survey": survey}
    else:
        response = {"status": "error", "message": "no rows found"}
    return HttpResponse(
        json.dumps(response), content_type="application/json", status=200
    )

@csrf_exempt
@api_view(["POST"])
def create_survey_user(request):
    """
    Creates a user with the provided username and name
    """
    try:
        request_body = json.loads(request.body.decode("utf-8"))
        username = request_body["username"]
        name = request_body["name"]
        try:
            SurveyUser.objects.get(Q(username=username))
        except SurveyUser.DoesNotExist:
            user = SurveyUser.objects.create(username=username, name=name)
            user.save()
            response = {"status": "success"}
            return HttpResponse(
                json.dumps(response), content_type="application/json", status=200
            )
        response = {"status": "error", "message": "User already exists"}
        return HttpResponse(json.dumps(response), "application/json", status=400)
    except KeyError as e:
        response = {"status": "error", "message": e}
        return HttpResponse(json.dumps(response), "application/json", status=400)

