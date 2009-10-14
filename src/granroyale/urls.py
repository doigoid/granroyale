from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 
     'django.views.generic.simple.direct_to_template',
     {'template':'index.html'}, name='index'),
                  
)

if settings.DEBUG:
    
    static_url = settings.MEDIA_URL
    if static_url.startswith('/'):
        static_url = static_url.lstrip('/')

    print settings.MEDIA_ROOT
    
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % static_url, 
         'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT,
          'show_indexes':True}),
    )
