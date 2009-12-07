
from south.db import db
from django.db import models
from granroyale.products.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.description'
        db.add_column('products_photo', 'description', orm['products.photo:description'])
        
        # Changing field 'CompleteBike.classification'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['products.ProductClass']))
        db.alter_column('products_completebike', 'classification_id', orm['products.completebike:classification'])
        
        # Changing field 'Part.classification'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['products.ProductClass']))
        db.alter_column('products_part', 'classification_id', orm['products.part:classification'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Photo.description'
        db.delete_column('products_photo', 'description')
        
        # Changing field 'CompleteBike.classification'
        # (to signature: django.db.models.fields.related.ForeignKey(null=True, to=orm['products.ProductClass'], blank=True))
        db.alter_column('products_completebike', 'classification_id', orm['products.completebike:classification'])
        
        # Changing field 'Part.classification'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['products.ProductClass']))
        db.alter_column('products_part', 'classification_id', orm['products.part:classification'])
        
    
    
    models = {
        'products.catalog': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': "'2009'", 'unique': 'True'})
        },
        'products.completebike': {
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Catalog']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductCategory']"}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'completebike'", 'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Photo']", 'null': 'True', 'blank': 'True'}),
            'product_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'small_product_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.part': {
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Catalog']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductCategory']"}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'part'", 'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Type']"}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Photo']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.photo': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_photo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'original_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'parent_photo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'angles'", 'blank': 'True', 'null': 'True', 'to': "orm['products.Photo']"}),
            'parts_pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Type']", 'null': 'True', 'blank': 'True'}),
            'pool': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'products.productcategory': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'products.productclass': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.softgood': {
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Catalog']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Photo']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'products.type': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['products.Type']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'softgood': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        }
    }
    
    complete_apps = ['products']
