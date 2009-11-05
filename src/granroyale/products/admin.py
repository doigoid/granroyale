from django.contrib import admin

from granroyale.products import models

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('title', 'pool', 'main_photo')
    
    def save_model(self, request, obj, form, change):
        
        if obj.main_photo and change:
            
            for product in obj.products.all():

                photos = product.photos.filter(main_photo=True)

                for photo in photos:
                    photo.main_photo = False
                    photo.save()
                    
        super(PhotoAdmin, self).save_model(request,obj,form,change)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }

admin.site.register(models.CompleteBike, ProductAdmin)
admin.site.register(models.SoftGood, ProductAdmin)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Type, ProductAdmin)
admin.site.register(models.Part, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductClass)
admin.site.register(models.Catalog)
