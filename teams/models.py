from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=255)

class RiallyUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    team = models.ForeignKey(Team)
    is_team_captain = models.BooleanField()

admin.site.register(Team)
admin.site.register(RiallyUser)
