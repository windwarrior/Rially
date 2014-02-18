from django.db import models
from django.contrib import admin

class Submission(models.Model):
    photo = models.ImageField(upload_to="submissions/")

    assignment = models.ForeignKey('Assignment')
    modifiers = models.ManyToManyField('Modifier')

    def __str__(self):
        return self.assignment.title

class Assignment(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Modifier(models.Model):
    modifier = models.CharField(max_length=255)

    def __str__(self):
        return self.modifier

admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Modifier)
