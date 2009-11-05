from django.conf.urls.defaults import patterns, include, url

import models

info_dicts = {

    'dealers': models.Dealer.objects.all(),
    
}

urlpatterns = patterns('',
    
    url(r'', 
        'django.views.generic.list_detail.object_list',
        {'queryset': info_dicts['dealers']},
        name='dealers'),
                      
)
