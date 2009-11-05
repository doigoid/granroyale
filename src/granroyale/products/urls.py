from django.conf.urls.defaults import patterns, include, url

import models

info_dicts = {

    'bikes': models.CompleteBike.objects.public(),
    'parts': models.Part.objects.public(),
    'softgoods': models.SoftGood.objects.public(),
    
}

urlpatterns = patterns('',
    
    url(r'^bikes/$', 
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['bikes']},
        name='products_completebikes'),

    url(r'^bikes/(?P<slug>[\w-]+)$',
        'django.views.generic.list_detail.object_detail',
        {'queryset': info_dicts['bikes']},
        name='products_completebikes_view'),

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
