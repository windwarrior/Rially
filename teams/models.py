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

class TemporaryUser(models.Model):
    """
        A user that hasn't confirmed its email yet and therefore is no
        real user object
    """
    email = models.EmailField()
    email_link = models.SlugField(max_length=128)
    team = models.ForeignKey(Team)
    becomes_team_captain = models.BooleanField(default=False)

admin.site.register(Team)
admin.site.register(RiallyUser)
