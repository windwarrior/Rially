from django.db import models
from django.contrib import admin

class Submission(models.Model):
    photo = models.ImageField(upload_to="submissions/")

    assignment = models.ForeignKey('Assignment')
    modifiers = models.ManyToManyField('Modifier')

class Assignment(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

class Modifier(models.Model):
    modifier = models.CharField(max_length=255)

    def __unicode__(self):
        return self.modifier

    def __str__(self):
        return self.__unicode__()

admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Modifier)
