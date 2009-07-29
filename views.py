# -*- coding: utf-8 -*-

from django.conf import settings

from snippets import render_to
from collection import models as models_coll
from collection import views as views_coll
from mediastore import models as models_media
from mediastore import views as views_media

def common_context(request):
    """ Общий контекст. """
    context = {}
    return context

@render_to('content.html', common_context)
def show_list(request, collection):
    """ Отображение страницы со списком событий. """
    opts = {
        'event': {
            'title': u'События',
            'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'band')},
                             {'title': u'Медиа', 'list': ['x', 'y', 'z']}]
            },
        'band': {
            'title': u'Группы',
            'section_list': [{'title': u'События', 'list': views_coll.get('list', 'event')},
                             {'title': u'Медиа', 'list': ['x', 'y', 'z']}]
            }
        }

    val = opts[collection]
    list = views_coll.get('list', collection)
    if collection == 'event':
        list = list.order_by('-when')

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
            'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'band')},
                             {'title': u'Медиа', 
                              'list': views_coll.related(models_coll.Event.objects.get(id=id), 
                                                         models_media.Photo)}]
            },
        'band': {
            'title': u'Группа',
            'section_list': [{'title': u'События', 'list': views_coll.get('list', 'event')},
                             {'title': u'Медиа', 'list': ['x', 'y', 'z']}]
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
    opts = {
        'photo': {
            'title': u'Фотография',
            'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'band')},
                             {'title': u'События', 'list': views_coll.get('list', 'event')}]
            },
        'video': {
            'title': u'Видео',
            'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'band')},
                             {'title': u'События', 'list': views_coll.get('list', 'event')}]
            },
        'audio': {
            'title': u'Аудио',
            'section_list': [{'title': u'Группы', 'list': views_coll.get('list', 'band')},
                             {'title': u'События', 'list': views_coll.get('list', 'event')}]
            },
        }

    val = opts[collection]

    context = {'mode': 'item',
               'item': views_media.get('item', collection, id),
               'item_type': val['title'],
               'section_list': val['section_list']
               }
    return context

