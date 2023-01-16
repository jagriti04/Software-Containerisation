from django.contrib import admin

from .models import SurveyUser, Questions, Choices, Survey, UserResponse

# # Register your models here.

@admin.register(SurveyUser, UserResponse)
class SurveyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Survey, Questions, Choices)
class SurveyAdmin(admin.ModelAdmin):
    pass

