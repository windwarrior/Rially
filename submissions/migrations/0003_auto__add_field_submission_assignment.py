# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Submission.assignment'
        db.add_column('submissions_submission', 'assignment',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submissions.Assignment'], default=''),
                      keep_default=False)

        # Adding M2M table for field modifiers on 'Submission'
        m2m_table_name = db.shorten_name('submissions_submission_modifiers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('submission', models.ForeignKey(orm['submissions.submission'], null=False)),
            ('modifier', models.ForeignKey(orm['submissions.modifier'], null=False))
        ))
        db.create_unique(m2m_table_name, ['submission_id', 'modifier_id'])


    def backwards(self, orm):
        # Deleting field 'Submission.assignment'
        db.delete_column('submissions_submission', 'assignment_id')

        # Removing M2M table for field modifiers on 'Submission'
        db.delete_table(db.shorten_name('submissions_submission_modifiers'))


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
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['submissions.Assignment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['submissions.Modifier']", 'symmetrical': 'False'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['submissions']