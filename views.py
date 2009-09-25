# -*- coding: utf-8 -*-

from django.conf import settings

from utils import related
from snippets import render_to
from collection import models as models_coll
from collection import views as views_coll
from mediastore import models as models_media
from mediastore import views as views_media

def common_context(request):
    """ Общий контекст. """
    context = {
        'debug': settings.DEBUG,
        'google_analytics': settings.GOOGLE_ANALYTICS,
        'media_url': settings.MEDIA_URL,
               }
    return context

@render_to('content.html', common_context)
def show_list(request, collection):
    """ Отображение страницы со списком событий. """
    opts = {
        'event': {
            'title': u'События',
            'section_list': [{'title': u'Проекты', 'list': views_coll.get('list', 'project')},
                             {'title': u'Медиа', 'list': ['x', 'y', 'z']}]
            },
        'project': {
            'title': u'Проекты',
            'section_list': [{'title': u'События', 'list': views_coll.get('list', 'event')},
                             {'title': u'Медиа', 'list': ['x', 'y', 'z']}]
            }
        }

    val = opts[collection]
    list = views_coll.get('list', collection)

    context = {'mode': 'list', 'collection': collection,
               'item_list': list,
               'list_title': val['title'],
               'section_list': val['section_list']
               }
    return context

@render_to('content.html', common_context)
def show_item(request, collection, id):
    """ Отображение страницы с элементом. """
    opts = {
        'event': {
            'title': u'Событие',
            'section_list': [{'title': u'Проекты', 'list': views_coll.get('list', 'project')},
                             {'title': u'Медиа', 'list': related(models_coll.Event, id, models_media.Photo)}]
            },
        'project': {
            'title': u'Проект',
            'section_list': [{'title': u'События', 'list': views_coll.get('list', 'event')},
                             {'title': u'Медиа', 'list': related(models_coll.Band, id, models_media.Photo)}]
            }
        }

    val = opts[collection]

    context = {'mode': 'item',
               'item': views_coll.get('item', collection, id),
               'item_type': val['title'],
               'section_list': val['section_list']
               }
    return context

@render_to('content.html', common_context)
def show_item_media(request, collection, id):
    """ Отображение страницы с элементом. """
    opts = {'photo': {'title': u'Фотография', },
            'video': {'title': u'Видео', },
            'audio': {'title': u'Аудио', }}
    val = opts[collection]
    val.update({'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'project')},
                                 {'title': u'События', 'list': views_coll.get('list', 'event')}]})
    context = {'mode': 'item',
               'item': views_media.get('item', collection, id),
               'item_type': val['title'],
               'section_list': val['section_list']
               }
    return context

