from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from photologue.models import Photo

class Catalog(models.Model):

    year = models.IntegerField(_('Catalog year'),
                                 default=str(date.today().year),
                                 unique=True)
    description = models.TextField(_('Short description about this catalog'),
                                   blank=True)
    public = models.BooleanField(_('Allow this catalog and its products to be visible?'),
                                 default=True)

    def __unicode__(self):
        return str(self.year)

class Product(models.Model):

    name = models.CharField(_('Product name'), max_length=50)
    catalog = models.ManyToManyField(Catalog, related_name="%(class)s")

    description = models.TextField(_('Description'), blank=True)

    inventory = models.CharField(_('Internal inventory information'),
                                 max_length=500, blank=True)   
    msrp = models.DecimalField(_('MSRP cost'),
                               max_digits=6, decimal_places=2, blank=True, null=True)

    colors = models.CharField(max_length=250, blank=True)
    public = models.BooleanField(default=True)

    photos = models.ManyToManyField(Photo, related_name='%(class)s', blank=True, null=True)
    
    class Meta:
        abstract = True
        ordering = ['-msrp',]
        
    def __unicode__(self):
        return self.name

class ProductClass(models.Model):

    name = models.CharField(_('Product type title'), max_length=50)
    position = models.IntegerField(_('Ordering position'))
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        ordering = ['position']
    
    def __unicode__(self):
        return self.name

class ProductCategory(models.Model):

    name = models.CharField(_('Product type title'), max_length=50)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class HardGood (Product):

    classes = models.ManyToManyField(ProductClass, related_name='%(class)s')
    categories = models.ManyToManyField(ProductCategory, related_name='%(class)s')
    
    features = models.TextField(blank=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sizes = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True

class PartType(models.Model):

    name = models.CharField(_('Name'), max_length=50)
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    description = models.TextField(_('Description'), blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Part(HardGood):

    part_type = models.ForeignKey(PartType)
    
    class Meta:
        ordering = ['name']
    
class CompleteBike(HardGood):

	components = models.ManyToManyField(Part, blank=True, null=True)
	top_tube_sizes = models.CharField(max_length=250, blank=True)

	showcase_image = models.ImageField(upload_to="products/completes/showcase/")
	product_logo = models.ImageField(upload_to="products/completes/logos/")

class Frame(HardGood):

	top_tube_sizes = models.CharField(max_length=250, blank=True)
	showcase_image = models.ImageField(upload_to="products/frames/showcase/")
	product_logo = models.ImageField(upload_to="products/frames/logos/")
	
class SoftGood(Product):

    class Meta:
        ordering = ['name']
