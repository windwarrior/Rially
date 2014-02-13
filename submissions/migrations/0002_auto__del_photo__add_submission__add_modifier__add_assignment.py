# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table('submissions_photo')

        # Adding model 'Submission'
        db.create_table('submissions_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('submissions', ['Submission'])

        # Adding model 'Modifier'
        db.create_table('submissions_modifier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modifier', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('submissions', ['Modifier'])

        # Adding model 'Assignment'
        db.create_table('submissions_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('submissions', ['Assignment'])


    def backwards(self, orm):
        # Adding model 'Photo'
        db.create_table('submissions_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('submissions', ['Photo'])

        # Deleting model 'Submission'
        db.delete_table('submissions_submission')

        # Deleting model 'Modifier'
        db.delete_table('submissions_modifier')

        # Deleting model 'Assignment'
        db.delete_table('submissions_assignment')


    models = {
        'submissions.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'submissions.modifier': {
            'Meta': {'object_name': 'Modifier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'submissions.submission': {
            'Meta': {'object_name': 'Submission'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['submissions']