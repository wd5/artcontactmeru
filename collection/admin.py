# -*- coding: utf-8 -*-

from django.contrib import admin

from collection import models
from mediastore.admin import PhotoInline

class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'reg_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title', 'desc', 'fname', 'iname', 'oname')}),)
admin.site.register(models.Person, PersonAdmin)

class BandAdmin(admin.ModelAdmin):
    model = models.Band
    inlines = (PhotoInline, )
    list_display = ('title',)
    ordered = ('title',)
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title', 'desc')}),)
admin.site.register(models.Band, BandAdmin)

class EventAdmin(admin.ModelAdmin):
    model = models.Event
    inlines = (PhotoInline, )
    list_display = ('title', 'where', 'when')
    ordered = ('title',)
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title', 'desc', 'bands', 'when', 'where')}),)
admin.site.register(models.Event, EventAdmin)

