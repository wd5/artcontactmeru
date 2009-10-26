# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from mediastore import models

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    ordered = ('title', 'parent')
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title', 'parent')}),)
admin.site.register(models.Catalog, CatalogAdmin)

class PhotoInline(GenericTabularInline):
    model = models.Photo
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'slug', 'tags', 'file', 'order_num', 'is_main')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_num', 'upload_date', 'last_modification')
    ordering = ('order_num', 'title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': (('title', 'slug', 'order_num'), 'catalog', 'content_type', ('tags', 'is_main'), 'file', 'desc')}),)
admin.site.register(models.Photo, PhotoAdmin)

class VideoInline(GenericTabularInline):
    model = models.Video
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'slug', 'tags', 'youtube', 'order_num', 'is_main')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_num', 'upload_date', 'last_modification')
    ordering = ('order_num', 'title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': (('title', 'slug', 'order_num'), 'tags', 'youtube', 'desc')}),)
admin.site.register(models.Video, VideoAdmin)

class AudioInline(GenericTabularInline):
    model = models.Audio
    extra = 2
    ct_field_name = 'content_type'
    id_field_name = 'object_id'
    fields = ('title', 'slug', 'tags', 'file', 'order_num', 'is_main')

class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_num', 'upload_date', 'last_modification')
    ordered = ('order_num', 'title', 'last_modification')
    search_fields = ('title','tags')
    fieldsets = ((None, {'fields': (('title', 'slug', 'order_num'), 'tags', 'file', 'desc')}),)
admin.site.register(models.Audio, AudioAdmin)

