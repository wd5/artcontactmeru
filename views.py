# -*- coding: utf-8 -*-

import operator

from django.conf import settings

from utils import get_media
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
            'section_list': [ {'title': u'Проекты', 'list': views_coll.get('list', 'project')}, ]
            },
        'project': {
            'title': u'Проекты',
            'section_list': [ {'title': u'События', 'list': views_coll.get('list', 'event')}, ]
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
def show_item(request, collection, slug):
    """ Отображение страницы с элементом. """
    opts = {
        'event': {
            'title': u'Событие',
            'model': models_coll.Event,
            'section_list': [ {'title': u'Проекты', 'list': views_coll.get('list', 'project')}, ]
            },
        'project': {
            'title': u'Проект',
            'model': models_coll.Band,
            'section_list': [ {'title': u'События', 'list': views_coll.get('list', 'event')}, ]
            }
        }

    val = opts[collection]
    item = val['model'].objects.get(slug=slug)
    media = get_media(models_media, val['model'], item.id)
    media.sort(key=operator.attrgetter('order_num'))
    context = {'mode': 'item',
               'item': views_coll.get('item', collection, slug),
               'item_type': val['title'],
               'section_list': val['section_list'],
               'media': media
               }
    return context

@render_to('content.html', common_context)
def show_item_media(request, collection, slug):
    """ Отображение страницы с элементом. """
    opts = {'photo': {'title': u'Фотография', },
            'video': {'title': u'Видео', },
            'audio': {'title': u'Аудио', }}
    val = opts[collection]
    val.update({'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'project')},
                                 {'title': u'События', 'list': views_coll.get('list', 'event')}]})
    context = {'mode': 'item',
               'item': views_media.get('item', collection, slug),
               'item_type': val['title'],
               'section_list': val['section_list']
               }
    return context

