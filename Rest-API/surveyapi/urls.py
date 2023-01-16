from django.urls import path

from . import views

urlpatterns = [
    path('all-users/', views.users_list),
    path('<int:survey_version>/', views.survey_by_version),
    path('add-user/', views.create_survey_user),
]