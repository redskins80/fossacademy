# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Challenge.description'
        db.delete_column('challenges_challenge', 'description')

        # Deleting field 'Challenge.description_html'
        db.delete_column('challenges_challenge', 'description_html')

        # Adding field 'Challenge.title_long'
        db.add_column('challenges_challenge', 'title_long', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Challenge.brief'
        db.add_column('challenges_challenge', 'brief', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Challenge.guidelines'
        db.add_column('challenges_challenge', 'guidelines', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Challenge.important_dates'
        db.add_column('challenges_challenge', 'important_dates', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Challenge.resources'
        db.add_column('challenges_challenge', 'resources', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Challenge.rules'
        db.add_column('challenges_challenge', 'rules', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Challenge.description'
        db.add_column('challenges_challenge', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Challenge.description_html'
        db.add_column('challenges_challenge', 'description_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Challenge.title_long'
        db.delete_column('challenges_challenge', 'title_long')

        # Deleting field 'Challenge.brief'
        db.delete_column('challenges_challenge', 'brief')

        # Deleting field 'Challenge.guidelines'
        db.delete_column('challenges_challenge', 'guidelines')

        # Deleting field 'Challenge.important_dates'
        db.delete_column('challenges_challenge', 'important_dates')

        # Deleting field 'Challenge.resources'
        db.delete_column('challenges_challenge', 'resources')

        # Deleting field 'Challenge.rules'
        db.delete_column('challenges_challenge', 'rules')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'challenges.challenge': {
            'Meta': {'object_name': 'Challenge'},
            'brief': ('django.db.models.fields.TextField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'challenges'", 'to': "orm['users.UserProfile']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 3, 16, 10, 52, 41, 898566)', 'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'guidelines': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important_dates': ('django.db.models.fields.TextField', [], {}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'resources': ('django.db.models.fields.TextField', [], {}),
            'rules': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 3, 16, 10, 52, 41, 898385)'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_long': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'challenges.judge': {
            'Meta': {'unique_together': "(('challenge', 'user'),)", 'object_name': 'Judge'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['challenges.Challenge']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'judges'", 'to': "orm['users.UserProfile']"})
        },
        'challenges.submission': {
            'Meta': {'object_name': 'Submission'},
            'challenge': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['challenges.Challenge']", 'symmetrical': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': "orm['users.UserProfile']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 3, 16, 10, 52, 41, 903021)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['users.UserProfile']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 3, 16)', 'auto_now_add': 'True', 'blank': 'True'}),
            'detailed_description': ('django.db.models.fields.TextField', [], {}),
            'detailed_description_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'users.profiletag': {
            'Meta': {'object_name': 'ProfileTag', '_ormbases': ['taggit.Tag']},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tag_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['taggit.Tag']", 'unique': 'True', 'primary_key': 'True'})
        },
        'users.taggedprofile': {
            'Meta': {'object_name': 'TaggedProfile'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users_taggedprofile_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users_taggedprofile_items'", 'to': "orm['users.ProfileTag']"})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 3, 16)', 'auto_now_add': 'True', 'blank': 'True'}),
            'discard_welcome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['challenges']