from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # This will match any url of the form /lilguys/lilguy_name, where
    # lilguy_name is the name of a lilguy (matches any non / character).
    # This page will display all information about a guy.
    url(r'^lilguys/(?P<lilguy_name>[^/]+)/', 'guytracker.views.display_guy'),
    #url(r'^lilguys/', 'guytracker.views.display_all'),
    # Examples:
    # url(r'^$', 'littleguys.views.home', name='home'),
    # url(r'^littleguys/', include('littleguys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT}))
