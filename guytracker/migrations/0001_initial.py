# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lilguy'
        db.create_table('guytracker_lilguy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=22)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=200)),
            ('current_lon', self.gf('django.db.models.fields.FloatField')()),
            ('current_lat', self.gf('django.db.models.fields.FloatField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('guytracker', ['Lilguy'])

        # Adding model 'Chapter'
        db.create_table('guytracker_chapter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lilguy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guytracker.Lilguy'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('story_text', self.gf('django.db.models.fields.TextField')()),
            ('found_at_lon', self.gf('django.db.models.fields.FloatField')()),
            ('found_at_lat', self.gf('django.db.models.fields.FloatField')()),
            ('dropped_at_lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dropped_at_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True, blank=True)),
        ))
        db.send_create_signal('guytracker', ['Chapter'])


    def backwards(self, orm):
        # Deleting model 'Lilguy'
        db.delete_table('guytracker_lilguy')

        # Deleting model 'Chapter'
        db.delete_table('guytracker_chapter')


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