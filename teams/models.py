from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=255)

    def __str__(self):
        return self.team_name

class RiallyUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    team = models.ForeignKey(Team)
    is_team_captain = models.BooleanField()

    def __str__(self):
        return self.title

class TemporaryUser(models.Model):
    """
        A user that hasn't confirmed its email yet and therefore is no
        real user object
    """
    email = models.EmailField()
    email_link = models.SlugField(max_length=64)
    team = models.ForeignKey(Team)
    becomes_team_captain = models.BooleanField(default=False)

    def __str__(self):
        return self.email

admin.site.register(Team)
admin.site.register(RiallyUser)
admin.site.register(TemporaryUser)
