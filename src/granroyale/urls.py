from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin

from granroyale.products import models

admin.autodiscover()
info_dicts = {
    'bikes':     models.CompleteBike.objects.public(),
    'parts':     models.Part.objects.public(),
    'softgoods': models.SoftGood.objects.all(),
}

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('granroyale.products.urls')),

    url(r'^dealers/$', include('granroyale.dealers.urls')),
    
    url(r'^about/$', 
     'django.views.generic.simple.direct_to_template',
     {'template':'about.html'}, name='about'),
                       
    url(r'^$', 
     'django.views.generic.simple.direct_to_template',
     {'template':'index.html'}, name='home'),
                  
)

if settings.DEBUG:
    
    static_url = settings.MEDIA_URL
    if static_url.startswith('/'):
        static_url = static_url.lstrip('/')
    
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % static_url, 
         'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT,
          'show_indexes':True}),
    )
