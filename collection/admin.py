# -*- coding: utf-8 -*-

from django.contrib import admin

from collection import models
from mediastore.admin import PhotoInline, VideoInline, AudioInline

class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'reg_date', 'last_modification')
    ordering = ('order_num', 'title', 'last_modification')
    search_fields = ('title',)
    fieldsets = ((None, {'fields': (('title', 'order_num'), 'desc', 'fname', 'iname', 'oname')}),)
admin.site.register(models.Person, PersonAdmin)

class BandAdmin(admin.ModelAdmin):
    model = models.Band
    inlines = (PhotoInline, VideoInline, AudioInline)
    list_display = ('title', 'slug')
    ordering = ('order_num', 'title',)
    search_fields = ('title',)
    fieldsets = ((None, {'fields': (('title', 'slug', 'order_num'), 'desc')}),)
admin.site.register(models.Band, BandAdmin)

class EventAdmin(admin.ModelAdmin):
    model = models.Event
    inlines = (PhotoInline, VideoInline, AudioInline)
    list_display = ('title', 'where', 'when')
    ordering = ('order_num', 'title',)
    search_fields = ('title',)
    fieldsets = ((None, {'fields': (('title', 'slug', 'order_num'), 'desc', 'bands', 'when', 'where')}),)
admin.site.register(models.Event, EventAdmin)

