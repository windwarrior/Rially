from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible

from teams.models import Team

@python_2_unicode_compatible
class Submission(models.Model):
    photo = models.ImageField(upload_to="submissions/")
    assignment = models.ForeignKey('Assignment')
    modifiers = models.ManyToManyField('Modifier', blank=True)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.assignment.title

@python_2_unicode_compatible
class Assignment(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Modifier(models.Model):
    modifier = models.CharField(max_length=255)
    can_occur_multiple = models.BooleanField(default=False)

    def __str__(self):
        return self.modifier + (" (onbeperkt)" if self.can_occur_multiple else "")


admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Modifier)
