# -*- coding: utf-8 -*-

from django.db import models

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
    #photo = models.ForeignKey()
    members = models.ManyToManyField(Person, verbose_name=u'Состав')

    class Meta:
        verbose_name = u'Коллектив'
        verbose_name_plural = u'Коллективы'

    def get_absolute_url(self):
        return u'/band/%i/' % self.id

class Event(CommonEntity):
    """ Событие. """
    bands = models.ManyToManyField(Band, verbose_name=u'Участники')
    #photo = models.ForeignKey()
    when = models.DateField(verbose_name=u'Дата')
    where = models.CharField(verbose_name=u'Место проведения', max_length=256)

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def get_absolute_url(self):
        return u'/event/%i/' % self.id

