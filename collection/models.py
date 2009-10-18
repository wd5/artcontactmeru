# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from django.utils.html import escape

from snippets import translit
from mediastore.models import Photo, Video, Audio

# Определяем абстрактный класс для элемента коллекции
class CommonEntity(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=64)
    desc = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    reg_date = models.DateTimeField(verbose_name=u'Зарегистрирован', auto_now_add=True)
    last_modification = models.DateTimeField(verbose_name=u'Изменён', auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return unicode(self.title)

class Person(CommonEntity):
    """ Отдельная персона. """
    fname = models.CharField(verbose_name=u'Фамилия', max_length=64)
    iname = models.CharField(verbose_name=u'Имя', max_length=64)
    oname = models.CharField(verbose_name=u'Отчество', max_length=64, blank=True)
    #photo = models.ForeignKey()

    class Meta:
        verbose_name = u'Персона'
        verbose_name_plural = u'Персоны'

    def get_absolute_url(self):
        return u'/person/%i/' % self.id

class Band(CommonEntity):
    """ Группа, коллектив артистов. """
    members = models.ManyToManyField(Person, verbose_name=u'Состав')
    photo = generic.GenericRelation(Photo)
    slug = models.CharField(u'Транслит', max_length=255)

    class Meta:
        verbose_name = u'Коллектив'
        verbose_name_plural = u'Коллективы'

    def get_absolute_url(self):
        return u'/project/%s/' % self.slug

#     def save(self):
#         self.slug = translit(escape(self.title))
#         super(Band, self).save()

    def get_photo(self):
        qs = self.photo.filter(is_main=True)
        if qs:
            return qs[0]
        else:
            None

class Event(CommonEntity):
    """ Событие. """
    bands = models.ManyToManyField(Band, verbose_name=u'Участники')
    when = models.DateField(verbose_name=u'Дата')
    where = models.CharField(verbose_name=u'Место проведения', max_length=256)
    photo = generic.GenericRelation(Photo)

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def get_absolute_url(self):
        return u'/event/%i/' % self.id

    def get_photo(self):
        qs = self.photo.filter(is_main=True)
        if qs:
            return qs[0]
        else:
            None

