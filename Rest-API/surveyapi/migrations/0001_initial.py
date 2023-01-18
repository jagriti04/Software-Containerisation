# Generated by Django 3.2.16 on 2023-01-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(choices=[('MCQ', 'Multiple Choice Questions'), ('TEXT', 'Long text')], default='MCQ', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('survey_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('survey_version', models.IntegerField(default=0, unique=True)),
                ('number_of_questions', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyUser',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('ur_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
