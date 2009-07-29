# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from mediastore import models

class PhotoInline(GenericTabularInline):
    model = models.Photo
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'content_type', 'tags', 'file', 'desc')}),)
admin.site.register(models.Photo, PhotoAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'tags', 'file', 'desc')}),)
admin.site.register(models.Video, VideoAdmin)

class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'tags', 'file', 'desc')}),)
admin.site.register(models.Audio, AudioAdmin)

