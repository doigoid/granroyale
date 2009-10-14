from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageModel

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

class Photo(ImageModel):

    POOLS = [
        ('CompleteBike', 'Complete Bikes'),
        ('Part', 'Parts'),
        ('SoftGood', 'Soft Goods'),
    ]
    
    title = models.CharField(_('Photo title'), max_length=128)
    original_image = models.ImageField(upload_to='photos/products/')

    main_photo = models.BooleanField(_("Main photo for product"), default=False)

    pool = models.CharField(choices=POOLS, max_length=32)
    parts_pool = models.ForeignKey('PartType',
                                   help_text=_('If the photo is a part, what type of part is it of?'),
                                   blank=True, null=True)
    def __unicode__(self):
        return self.title
    
    class IKOptions:        
        spec_module = 'granroyale.products.imagespecs'
        cache_dir = 'photos'
        image_field = 'original_image'

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
    
    class Meta:
        abstract = True
        ordering = ['-msrp',]
        
    def __unicode__(self):
        return self.name

class ProductClass(models.Model):

    name = models.CharField(_('Product class'), max_length=50)
    position = models.IntegerField(_('Ordering position'))
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Product classes'
        
    def __unicode__(self):
        return self.name

class ProductCategory(models.Model):

    name = models.CharField(_('Product category'), max_length=50)
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
    photos = models.ManyToManyField(Photo, related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'Part'})   
    class Meta:
        ordering = ['name']
    
class CompleteBike(HardGood):

    components = models.ManyToManyField(Part, blank=True, null=True)
    top_tube_sizes = models.CharField(max_length=250, blank=True)
    
    showcase_image = models.ImageField(upload_to="products/completes/showcase/")
    product_logo = models.ImageField(upload_to="products/completes/logos/")
    photos = models.ManyToManyField(Photo, related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'CompleteBike'})
    
class SoftGood(Product):

    photos = models.ManyToManyField(Photo, related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'SoftGood'})
    
    class Meta:
        ordering = ['name']
