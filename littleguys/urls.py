#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#import dajaxice.core as dja
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import dajaxice.core as dja
from inspect import getmembers
#print getmembers(dja)

urlpatterns = patterns('',
    # This will match any url of the form /lilguys/lilguy_name, where
    # lilguy_name is the name of a lilguy (matches any non / character).
    # This page will display all information about a guy.
    url(r'^lilguys/(?P<url_code>[^/]+)/', 'guytracker.views.display_guy'),
    url(r'^lilguys*', 'guytracker.views.all_guys'),
    # Examples:
    # url(r'^$', 'littleguys.views.home', name='home'),
    # url(r'^littleguys/', include('littleguys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # AJAX endpoints here
    #url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT}))
