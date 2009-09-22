# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/(.*)', admin.site.root),

    url(r'^$', 'views.show_list', {'collection': 'event'}, name="events"),

    url(r'^events/$', 'views.show_list', {'collection': 'event'}, name="events"),
    url(r'^projects/$', 'views.show_list', {'collection': 'project'}, name="projects"),
    url(r'^medias/$', 'views.show_list', {'collection': 'media'}, name="medias"),

    url(r'^event/(?P<id>\d+)/$', 'views.show_item', {'collection': 'event'}, name="event"),
    url(r'^project/(?P<id>\d+)/$', 'views.show_item', {'collection': 'project'}, name="project"),
    url(r'^photo/(?P<id>\d+)/$', 'views.show_item_media', {'collection': 'photo'}, name="photo"),
)
