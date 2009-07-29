# -*- coding: utf-8 -*-

from django.http import Http404
from collection import models

def get(mode=None, collection=None, id=None):
    """ mode is ('list', 'item'), collection is ('band', 'event'), id if exists """
    handlers = {
        'event': models.Event,
        'band': models.Band
        }
    try:
        if mode == 'list':
            return handlers[collection].objects.all()
        else:
            return handlers[collection].objects.get(id=id)
    except (models.Event.DoesNotExist, models.Band.DoesNotExist, KeyError):
        raise Http404
 
