# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from tagging.fields import TagField

class Catalog(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=u'Предок')
    title = models.CharField(verbose_name=u'Заголовок', max_length=64)

    class Meta:
        verbose_name = u'Каталог'
        verbose_name_plural = u'Каталоги'

    def __unicode__(self):
        return self.title

# Абстрактная модель
class CommonMedia(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=64)
    desc = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    upload_date = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)
    last_modification = models.DateTimeField(verbose_name=u'Изменён', auto_now_add=True, auto_now=True)
    is_main = models.BooleanField(verbose_name=u'Это главный объект?')
    type = models.CharField(verbose_name=u'Тип', max_length=5)
    catalog = models.ForeignKey(Catalog, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=Q(model='person')|Q(model='band')|Q(model='event'))
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    tags = TagField(verbose_name=u'Теги объекта')

    class Meta:
        abstract = True

    def get_tag_list(self):
        from tagging.utils import parse_tag_input
        return parse_tag_input(self.tags)

class Photo(CommonMedia):
    file = models.FileField(verbose_name=u'Файл', upload_to=u'files/photo')

    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'

    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)
        self.type = 'photo'

    def get_absolute_url(self):
        return u'/photo/%i/' % self.id

class Video(CommonMedia):
    file = models.FileField(verbose_name=u'Файл', upload_to=u'files/video')

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)
        self.type = 'video'

    def get_absolute_url(self):
        return u'/video/%i/' % self.id

class Audio(CommonMedia):
    file = models.FileField(verbose_name=u'Файл', upload_to=u'files/audio')

    class Meta:
        verbose_name = u'Аудио'
        verbose_name_plural = u'Аудио'

    def __init__(self, *args, **kwargs):
        super(Audio, self).__init__(*args, **kwargs)
        self.type = 'audio'

    def get_absolute_url(self):
        return u'/audio/%i/' % self.id

