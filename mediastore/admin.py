# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from mediastore import models

class PhotoInline(GenericTabularInline):
    model = models.Photo
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'tags', 'file', 'is_main')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'content_type', ('tags', 'is_main'), 'file', 'desc')}),)
admin.site.register(models.Photo, PhotoAdmin)

class VideoInline(GenericTabularInline):
    model = models.Video
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'tags', 'file', 'is_main')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'tags', 'file', 'desc')}),)
admin.site.register(models.Video, VideoAdmin)

class AudioInline(GenericTabularInline):
    model = models.Audio
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'tags', 'file', 'is_main')

class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'last_modification')
    ordered = ('title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': ('title', 'tags', 'file', 'desc')}),)
admin.site.register(models.Audio, AudioAdmin)

