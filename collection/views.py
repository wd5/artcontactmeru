# -*- coding: utf-8 -*-

from django.http import Http404
from collection import models as c_models
from mediastore import models as m_models

def get(mode=None, collection=None, slug=None):
    """ mode is ('list', 'item'), collection is ('project', 'event'), id if exists """
    handlers = {
        'event': (c_models.Event, '-when'),
        'project': (c_models.Band, '-reg_date')
        }
    try:
        (model, sorting) = handlers[collection]
        if mode == 'list':
            return model.objects.all().order_by(sorting)
        else:
            return model.objects.get(slug=slug)
    except (c_models.Event.DoesNotExist, c_models.Band.DoesNotExist, KeyError):
        raise Http404
    
