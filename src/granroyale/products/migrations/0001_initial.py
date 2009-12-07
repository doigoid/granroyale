
from south.db import db
from django.db import models
from granroyale.products.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ProductClass'
        db.create_table('products_productclass', (
            ('id', orm['products.ProductClass:id']),
            ('name', orm['products.ProductClass:name']),
            ('position', orm['products.ProductClass:position']),
            ('description', orm['products.ProductClass:description']),
        ))
        db.send_create_signal('products', ['ProductClass'])
        
        # Adding model 'SoftGood'
        db.create_table('products_softgood', (
            ('id', orm['products.SoftGood:id']),
            ('name', orm['products.SoftGood:name']),
            ('slug', orm['products.SoftGood:slug']),
            ('description', orm['products.SoftGood:description']),
            ('inventory', orm['products.SoftGood:inventory']),
            ('msrp', orm['products.SoftGood:msrp']),
            ('colors', orm['products.SoftGood:colors']),
            ('public', orm['products.SoftGood:public']),
            ('created', orm['products.SoftGood:created']),
            ('updated', orm['products.SoftGood:updated']),
        ))
        db.send_create_signal('products', ['SoftGood'])
        
        # Adding model 'ProductCategory'
        db.create_table('products_productcategory', (
            ('id', orm['products.ProductCategory:id']),
            ('name', orm['products.ProductCategory:name']),
            ('description', orm['products.ProductCategory:description']),
        ))
        db.send_create_signal('products', ['ProductCategory'])
        
        # Adding model 'Catalog'
        db.create_table('products_catalog', (
            ('id', orm['products.Catalog:id']),
            ('year', orm['products.Catalog:year']),
            ('description', orm['products.Catalog:description']),
            ('public', orm['products.Catalog:public']),
        ))
        db.send_create_signal('products', ['Catalog'])
        
        # Adding model 'CompleteBike'
        db.create_table('products_completebike', (
            ('id', orm['products.CompleteBike:id']),
            ('name', orm['products.CompleteBike:name']),
            ('slug', orm['products.CompleteBike:slug']),
            ('description', orm['products.CompleteBike:description']),
            ('inventory', orm['products.CompleteBike:inventory']),
            ('msrp', orm['products.CompleteBike:msrp']),
            ('colors', orm['products.CompleteBike:colors']),
            ('public', orm['products.CompleteBike:public']),
            ('created', orm['products.CompleteBike:created']),
            ('updated', orm['products.CompleteBike:updated']),
            ('features', orm['products.CompleteBike:features']),
            ('weight', orm['products.CompleteBike:weight']),
            ('sizes', orm['products.CompleteBike:sizes']),
            ('product_logo', orm['products.CompleteBike:product_logo']),
            ('small_product_logo', orm['products.CompleteBike:small_product_logo']),
        ))
        db.send_create_signal('products', ['CompleteBike'])
        
        # Adding model 'Part'
        db.create_table('products_part', (
            ('id', orm['products.Part:id']),
            ('name', orm['products.Part:name']),
            ('slug', orm['products.Part:slug']),
            ('description', orm['products.Part:description']),
            ('inventory', orm['products.Part:inventory']),
            ('msrp', orm['products.Part:msrp']),
            ('colors', orm['products.Part:colors']),
            ('public', orm['products.Part:public']),
            ('created', orm['products.Part:created']),
            ('updated', orm['products.Part:updated']),
            ('features', orm['products.Part:features']),
            ('weight', orm['products.Part:weight']),
            ('sizes', orm['products.Part:sizes']),
            ('part_type', orm['products.Part:part_type']),
        ))
        db.send_create_signal('products', ['Part'])
        
        # Adding model 'Type'
        db.create_table('products_type', (
            ('id', orm['products.Type:id']),
            ('name', orm['products.Type:name']),
            ('slug', orm['products.Type:slug']),
            ('softgood', orm['products.Type:softgood']),
            ('parent', orm['products.Type:parent']),
            ('description', orm['products.Type:description']),
        ))
        db.send_create_signal('products', ['Type'])
        
        # Adding model 'Photo'
        db.create_table('products_photo', (
            ('id', orm['products.Photo:id']),
            ('title', orm['products.Photo:title']),
            ('original_image', orm['products.Photo:original_image']),
            ('main_photo', orm['products.Photo:main_photo']),
            ('parent_photo', orm['products.Photo:parent_photo']),
            ('pool', orm['products.Photo:pool']),
            ('parts_pool', orm['products.Photo:parts_pool']),
            ('created', orm['products.Photo:created']),
            ('updated', orm['products.Photo:updated']),
        ))
        db.send_create_signal('products', ['Photo'])
        
        # Adding ManyToManyField 'Part.photos'
        db.create_table('products_part_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('photo', models.ForeignKey(orm.Photo, null=False))
        ))
        
        # Adding ManyToManyField 'Part.categories'
        db.create_table('products_part_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('productcategory', models.ForeignKey(orm.ProductCategory, null=False))
        ))
        
        # Adding ManyToManyField 'SoftGood.catalog'
        db.create_table('products_softgood_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('softgood', models.ForeignKey(orm.SoftGood, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
        # Adding ManyToManyField 'SoftGood.photos'
        db.create_table('products_softgood_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('softgood', models.ForeignKey(orm.SoftGood, null=False)),
            ('photo', models.ForeignKey(orm.Photo, null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.photos'
        db.create_table('products_completebike_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('photo', models.ForeignKey(orm.Photo, null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.catalog'
        db.create_table('products_completebike_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.classes'
        db.create_table('products_completebike_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('productclass', models.ForeignKey(orm.ProductClass, null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.categories'
        db.create_table('products_completebike_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('productcategory', models.ForeignKey(orm.ProductCategory, null=False))
        ))
        
        # Adding ManyToManyField 'Part.classes'
        db.create_table('products_part_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('productclass', models.ForeignKey(orm.ProductClass, null=False))
        ))
        
        # Adding ManyToManyField 'Part.catalog'
        db.create_table('products_part_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'ProductClass'
        db.delete_table('products_productclass')
        
        # Deleting model 'SoftGood'
        db.delete_table('products_softgood')
        
        # Deleting model 'ProductCategory'
        db.delete_table('products_productcategory')
        
        # Deleting model 'Catalog'
        db.delete_table('products_catalog')
        
        # Deleting model 'CompleteBike'
        db.delete_table('products_completebike')
        
        # Deleting model 'Part'
        db.delete_table('products_part')
        
        # Deleting model 'Type'
        db.delete_table('products_type')
        
        # Deleting model 'Photo'
        db.delete_table('products_photo')
        
        # Dropping ManyToManyField 'Part.photos'
        db.delete_table('products_part_photos')
        
        # Dropping ManyToManyField 'Part.categories'
        db.delete_table('products_part_categories')
        
        # Dropping ManyToManyField 'SoftGood.catalog'
        db.delete_table('products_softgood_catalog')
        
        # Dropping ManyToManyField 'SoftGood.photos'
        db.delete_table('products_softgood_photos')
        
        # Dropping ManyToManyField 'CompleteBike.photos'
        db.delete_table('products_completebike_photos')
        
        # Dropping ManyToManyField 'CompleteBike.catalog'
        db.delete_table('products_completebike_catalog')
        
        # Dropping ManyToManyField 'CompleteBike.classes'
        db.delete_table('products_completebike_classes')
        
        # Dropping ManyToManyField 'CompleteBike.categories'
        db.delete_table('products_completebike_categories')
        
        # Dropping ManyToManyField 'Part.classes'
        db.delete_table('products_part_classes')
        
        # Dropping ManyToManyField 'Part.catalog'
        db.delete_table('products_part_catalog')
        
    
    
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
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Type']"}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Photo']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.photo': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
