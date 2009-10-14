
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
            ('description', orm['products.SoftGood:description']),
            ('inventory', orm['products.SoftGood:inventory']),
            ('msrp', orm['products.SoftGood:msrp']),
            ('colors', orm['products.SoftGood:colors']),
            ('public', orm['products.SoftGood:public']),
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
            ('description', orm['products.CompleteBike:description']),
            ('inventory', orm['products.CompleteBike:inventory']),
            ('msrp', orm['products.CompleteBike:msrp']),
            ('colors', orm['products.CompleteBike:colors']),
            ('public', orm['products.CompleteBike:public']),
            ('features', orm['products.CompleteBike:features']),
            ('weight', orm['products.CompleteBike:weight']),
            ('sizes', orm['products.CompleteBike:sizes']),
            ('top_tube_sizes', orm['products.CompleteBike:top_tube_sizes']),
            ('showcase_image', orm['products.CompleteBike:showcase_image']),
            ('product_logo', orm['products.CompleteBike:product_logo']),
        ))
        db.send_create_signal('products', ['CompleteBike'])
        
        # Adding model 'Part'
        db.create_table('products_part', (
            ('id', orm['products.Part:id']),
            ('name', orm['products.Part:name']),
            ('description', orm['products.Part:description']),
            ('inventory', orm['products.Part:inventory']),
            ('msrp', orm['products.Part:msrp']),
            ('colors', orm['products.Part:colors']),
            ('public', orm['products.Part:public']),
            ('features', orm['products.Part:features']),
            ('weight', orm['products.Part:weight']),
            ('sizes', orm['products.Part:sizes']),
            ('part_type', orm['products.Part:part_type']),
        ))
        db.send_create_signal('products', ['Part'])
        
        # Adding model 'PartType'
        db.create_table('products_parttype', (
            ('id', orm['products.PartType:id']),
            ('name', orm['products.PartType:name']),
            ('parent', orm['products.PartType:parent']),
            ('description', orm['products.PartType:description']),
        ))
        db.send_create_signal('products', ['PartType'])
        
        # Adding model 'Frame'
        db.create_table('products_frame', (
            ('id', orm['products.Frame:id']),
            ('name', orm['products.Frame:name']),
            ('description', orm['products.Frame:description']),
            ('inventory', orm['products.Frame:inventory']),
            ('msrp', orm['products.Frame:msrp']),
            ('colors', orm['products.Frame:colors']),
            ('public', orm['products.Frame:public']),
            ('features', orm['products.Frame:features']),
            ('weight', orm['products.Frame:weight']),
            ('sizes', orm['products.Frame:sizes']),
            ('top_tube_sizes', orm['products.Frame:top_tube_sizes']),
            ('showcase_image', orm['products.Frame:showcase_image']),
            ('product_logo', orm['products.Frame:product_logo']),
        ))
        db.send_create_signal('products', ['Frame'])
        
        # Adding ManyToManyField 'CompleteBike.components'
        db.create_table('products_completebike_components', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('part', models.ForeignKey(orm.Part, null=False))
        ))
        
        # Adding ManyToManyField 'Part.photos'
        db.create_table('products_part_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('photo', models.ForeignKey(orm['photologue.Photo'], null=False))
        ))
        
        # Adding ManyToManyField 'Part.categories'
        db.create_table('products_part_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('part', models.ForeignKey(orm.Part, null=False)),
            ('productcategory', models.ForeignKey(orm.ProductCategory, null=False))
        ))
        
        # Adding ManyToManyField 'Frame.catalog'
        db.create_table('products_frame_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('frame', models.ForeignKey(orm.Frame, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
        # Adding ManyToManyField 'SoftGood.catalog'
        db.create_table('products_softgood_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('softgood', models.ForeignKey(orm.SoftGood, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
        # Adding ManyToManyField 'Frame.classes'
        db.create_table('products_frame_classes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('frame', models.ForeignKey(orm.Frame, null=False)),
            ('productclass', models.ForeignKey(orm.ProductClass, null=False))
        ))
        
        # Adding ManyToManyField 'SoftGood.photos'
        db.create_table('products_softgood_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('softgood', models.ForeignKey(orm.SoftGood, null=False)),
            ('photo', models.ForeignKey(orm['photologue.Photo'], null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.photos'
        db.create_table('products_completebike_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('photo', models.ForeignKey(orm['photologue.Photo'], null=False))
        ))
        
        # Adding ManyToManyField 'Frame.photos'
        db.create_table('products_frame_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('frame', models.ForeignKey(orm.Frame, null=False)),
            ('photo', models.ForeignKey(orm['photologue.Photo'], null=False))
        ))
        
        # Adding ManyToManyField 'CompleteBike.catalog'
        db.create_table('products_completebike_catalog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('completebike', models.ForeignKey(orm.CompleteBike, null=False)),
            ('catalog', models.ForeignKey(orm.Catalog, null=False))
        ))
        
        # Adding ManyToManyField 'Frame.categories'
        db.create_table('products_frame_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('frame', models.ForeignKey(orm.Frame, null=False)),
            ('productcategory', models.ForeignKey(orm.ProductCategory, null=False))
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
        
        # Deleting model 'PartType'
        db.delete_table('products_parttype')
        
        # Deleting model 'Frame'
        db.delete_table('products_frame')
        
        # Dropping ManyToManyField 'CompleteBike.components'
        db.delete_table('products_completebike_components')
        
        # Dropping ManyToManyField 'Part.photos'
        db.delete_table('products_part_photos')
        
        # Dropping ManyToManyField 'Part.categories'
        db.delete_table('products_part_categories')
        
        # Dropping ManyToManyField 'Frame.catalog'
        db.delete_table('products_frame_catalog')
        
        # Dropping ManyToManyField 'SoftGood.catalog'
        db.delete_table('products_softgood_catalog')
        
        # Dropping ManyToManyField 'Frame.classes'
        db.delete_table('products_frame_classes')
        
        # Dropping ManyToManyField 'SoftGood.photos'
        db.delete_table('products_softgood_photos')
        
        # Dropping ManyToManyField 'CompleteBike.photos'
        db.delete_table('products_completebike_photos')
        
        # Dropping ManyToManyField 'Frame.photos'
        db.delete_table('products_frame_photos')
        
        # Dropping ManyToManyField 'CompleteBike.catalog'
        db.delete_table('products_completebike_catalog')
        
        # Dropping ManyToManyField 'Frame.categories'
        db.delete_table('products_frame_categories')
        
        # Dropping ManyToManyField 'CompleteBike.classes'
        db.delete_table('products_completebike_classes')
        
        # Dropping ManyToManyField 'CompleteBike.categories'
        db.delete_table('products_completebike_categories')
        
        # Dropping ManyToManyField 'Part.classes'
        db.delete_table('products_part_classes')
        
        # Dropping ManyToManyField 'Part.catalog'
        db.delete_table('products_part_catalog')
        
    
    
    models = {
        'photologue.photo': {
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo_related'", 'blank': 'True', 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.59999999999999998'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
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
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Part']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'}),
            'product_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'showcase_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'top_tube_sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.frame': {
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Catalog']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductCategory']"}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'}),
            'product_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'showcase_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'top_tube_sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.part': {
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Catalog']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductCategory']"}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.ProductClass']"}),
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.PartType']"}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'products.parttype': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['products.PartType']"})
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'msrp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['products']
