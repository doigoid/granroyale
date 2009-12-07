from django.conf.urls.defaults import patterns, include, url

import models

info_dicts = {

    'bikes': models.CompleteBike.objects.public(),
    'mens_bikes': models.CompleteBike.objects.public().filter(
        classification__name__istartswith="men"),
    'womens_bikes': models.CompleteBike.objects.public().filter(
        classification__name__istartswith="women"),
    'parts': models.Part.objects.public(),
    'softgoods': models.SoftGood.objects.public(),
    
}

urlpatterns = patterns('',

    
    url(r'^bikes/$', 
        'django.views.generic.simple.direct_to_template',
        {'template': 'products/completebike_list.html'},
        name='products_completebikes'),
                       
    url(r'^bikes/mens/$', 
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['mens_bikes'],
         'template_name': 'products/completebike_list_mens.html'},
        name='products_completebikes_mens'),

    url(r'^bikes/womens/$', 
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['womens_bikes'],
         'template_name': 'products/completebike_list_womens.html'},
        name='products_completebikes_womens'),

    url(r'^bikes/mens/(?P<slug>[\w-]+)$',
        'django.views.generic.list_detail.object_detail',
        {'queryset': info_dicts['mens_bikes']},
        name='products_completebikes_mens_view'),
    
    url(r'^bikes/womens/(?P<slug>[\w-]+)$',
        'django.views.generic.list_detail.object_detail',
        {'queryset': info_dicts['womens_bikes']},
        name='products_completebikes_womens_view'),
    
    url(r'^accessories/$',
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['parts']},
        name='products_parts'),

    url(r'^accessories/(?P<slug>[\w-]+)$',
        'django.views.generic.list_detail.object_detail',
        {'queryset': info_dicts['parts']},
        name='products_parts_view'),
                       
    url(r'^softgoods/$',
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['softgoods']},
        name='products_softgoods'),

    url(r'^softgoods/(?P<slug>[\w-]+)$',
        'django.views.generic.list_detail.object_detail',
        {'queryset': info_dicts['softgoods']},
        name='products_softgoods_view'),
                       
)
