# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crash'
        db.create_table(u'bugs_crash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='crashes', to=orm['downloads.Application'])),
            ('build', self.gf('django.db.models.fields.IntegerField')()),
            ('report', self.gf('django.db.models.fields.TextField')()),
            ('crdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('tstamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_solved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_obsolete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bugs', ['Crash'])


    def backwards(self, orm):
        # Deleting model 'Crash'
        db.delete_table(u'bugs_crash')


    models = {
        u'bugs.crash': {
            'Meta': {'ordering': "('-build', '-crdate', '-tstamp')", 'object_name': 'Crash'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crashes'", 'to': u"orm['downloads.Application']"}),
            'build': ('django.db.models.fields.IntegerField', [], {}),
            'crdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_obsolete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_solved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'report': ('django.db.models.fields.TextField', [], {}),
            'tstamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'downloads.application': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['bugs']