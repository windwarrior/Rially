from django.db import models
from django.contrib import admin

from teams.models import Team

class Submission(models.Model):
    photo = models.ImageField(upload_to="submissions/")
    assignment = models.ForeignKey('Assignment')
    modifiers = models.ManyToManyField('Modifier', blank=True)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.assignment.title

class Assignment(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Modifier(models.Model):
    modifier = models.CharField(max_length=255)
    can_occur_multiple = models.BooleanField(default=False)

    def __str__(self):
        return self.modifier + (" (onbeperkt)" if self.can_occur_multiple else "")


admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Modifier)
