# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Chapter.picture_600'
        db.add_column('guytracker_chapter', 'picture_600',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Chapter.picture_600'
        db.delete_column('guytracker_chapter', 'picture_600')


    models = {
        'guytracker.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'dropped_at_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dropped_at_lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'found_at_lat': ('django.db.models.fields.FloatField', [], {}),
            'found_at_lon': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lilguy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guytracker.Lilguy']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'picture_600': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'story_text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        },
        'guytracker.lilguy': {
            'Meta': {'object_name': 'Lilguy'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '22'}),
            'current_lat': ('django.db.models.fields.FloatField', [], {}),
            'current_lon': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['guytracker']