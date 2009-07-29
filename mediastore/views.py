# -*- coding: utf-8 -*-

from django.http import Http404
from mediastore import models

def get(mode=None, collection=None, id=None):
    """ mode is ('list', 'item'), collection is ('photo', 'video', audio), id if exists """
    handlers = {
        'photo': models.Photo,
        'video': models.Video,
        'audio': models.Audio
        }
    try:
        if mode == 'list':
            return handlers[collection].objects.all()
        else:
            return handlers[collection].objects.get(id=id)
    except (models.Photo.DoesNotExist, models.Video.DoesNotExist, models.Audio.DoesNotExist, KeyError):
        raise Http404
 
