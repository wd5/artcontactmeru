# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/events/'}),
    url(r'^events/$', 'views.show_list', {'collection': 'event'}, name="events"),
    url(r'^bands/$', 'views.show_list', {'collection': 'band'}, name="groups"),
    url(r'^medias/$', 'views.show_list', {'collection': 'media'}, name="medias"),
    url(r'^event/(?P<id>\d+)/$', 'views.show_item', {'collection': 'event'}, name="event"),
    url(r'^band/(?P<id>\d+)/$', 'views.show_item', {'collection': 'band'}, name="group"),
    url(r'^media/(?P<id>\d+)/$', 'views.show_item', {'collection': 'media'}, name="media"),
)
