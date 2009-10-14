from django.contrib import admin

from granroyale.products import models

admin.site.register(models.CompleteBike)
admin.site.register(models.SoftGood)
admin.site.register(models.Frame)
admin.site.register(models.PartType)
admin.site.register(models.Part)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductClass)
admin.site.register(models.Catalog)
