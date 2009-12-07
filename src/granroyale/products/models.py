from datetime import date

from django.db import models
from django.contrib.contenttypes.models import ContentType
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

class ProductManager(models.Manager):

    def public(self, **kwargs):
        
        kwargs['public'] = True

        return super(ProductManager, self).filter(**kwargs)

    
class Product(models.Model):

    name = models.CharField(_('Product name'), max_length=50)
    catalog = models.ManyToManyField(Catalog, related_name="%(class)s")

    slug = models.SlugField()

    description = models.TextField(_('Description'), blank=True)

    inventory = models.CharField(_('Internal inventory information'),
                                 max_length=500, blank=True)   
    msrp = models.DecimalField(_('MSRP cost'),
                               max_digits=6, decimal_places=2, blank=True, null=True)

    colors = models.CharField(max_length=250, blank=True)
    public = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    pdf = models.FileField(_('Printable PDF'), upload_to='products/pdf/',
                           blank=True, null=True)

    objects = ProductManager()
    
    class Meta:
        abstract = True
        ordering = ['-msrp',]
        
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
         subclass = self.__class__.__name__.lower()
         return ('products_%ss_view' % subclass, (), {'slug': self.slug})

    
    @property
    def display_photo(self):

        try:
            return self.photos.filter(main_photo=True).order_by("-created")[0]
        except Exception:

            # if no main_photo is set, then return first in set
            
            return None

    def primary_photos(self):
        return self.photos.filter(parent_photo=None)

    def secondary_photos(self):
        return self.photos.filter(parent_photo__isnull=False)
    
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

    classification = models.ForeignKey(ProductClass, related_name='%(class)s')
    categories = models.ManyToManyField(ProductCategory, related_name='%(class)s')
    
    features = models.TextField(blank=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sizes = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True

class Type(models.Model):

    name = models.CharField(_('Name'), max_length=50)

    slug = models.SlugField()

    softgood = models.BooleanField(_('Is this is soft good type?'))
    
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    description = models.TextField(_('Description'), blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

# PRODUCT TYPES

class Part(HardGood):

    part_type = models.ForeignKey(Type)
    photos = models.ManyToManyField('Photo', related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'Part'})   
    class Meta:
        ordering = ['name']

    
class CompleteBike(HardGood):

    product_logo = models.ImageField(upload_to="products/completes/logos/")
    small_product_logo = models.ImageField(upload_to="products/completes/logos/")
    
    photos = models.ManyToManyField('Photo', related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'CompleteBike'})
                                    
    @models.permalink
    def get_absolute_url(self):
        return ('products_completebikes_%s_view' % str(self.classification), (), {
            'slug': self.slug
        })
    
    
    
class SoftGood(Product):

    photos = models.ManyToManyField('Photo', related_name='%(class)s',
                                    blank=True, null=True,
                                    limit_choices_to={'pool':'SoftGood'})
    class Meta:
        ordering = ['name']

    
class Photo(ImageModel):

    POOLS = [
        ('CompleteBike', 'Complete Bikes'),
        ('Part', 'Parts'),
        ('SoftGood', 'Soft Goods'),
    ]
    
    title = models.CharField(_('Photo title'), max_length=128)
    original_image = models.ImageField(upload_to='photos/products/')

    main_photo = models.BooleanField(_("Main photo for product"), default=False)

    parent_photo = models.ForeignKey('self', related_name="angles", null=True, blank=True,)
    
    pool = models.CharField(choices=POOLS, max_length=32)
    parts_pool = models.ForeignKey('Type',
                                   help_text=_('If the photo is a part, what type of part is it of?'),
                                   blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pool', 'title',)
    
    def __unicode__(self):
        return self.title

    @property
    def angleshot(self):
        return self.parent_photo is not None

    @property
    def products(self):
        """ Alias for the reverse relations of product photos """
        
        if self.pool == 'CompleteBike':
            return self.completebike
        elif self.pool == 'Part':
            return self.part
        elif self.pool == 'SoftGood':
            return self.softgood
        else:
            return None

    @property
    def thumb(self):
        if self.original_image.height >= self.original_image.width:
            return self.v_thumbnail_image
        else:
            return self.h_thumbnail_image
    
    class IKOptions:        
        spec_module = 'granroyale.products.imagespecs'
        cache_dir = 'photos'
        image_field = 'original_image'
