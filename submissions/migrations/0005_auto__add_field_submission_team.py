# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.team'
        db.add_column('submissions_submission', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'], default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.team'
        db.delete_column('submissions_submission', 'team_id')


    models = {
        'submissions.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'submissions.modifier': {
            'Meta': {'object_name': 'Modifier'},
            'can_occur_multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'submissions.submission': {
            'Meta': {'object_name': 'Submission'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['submissions.Assignment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['submissions.Modifier']", 'blank': 'True', 'symmetrical': 'False'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['submissions']