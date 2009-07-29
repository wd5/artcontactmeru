# -*- coding: utf-8 -*-

from django.http import Http404
from collection import models as c_models
from mediastore import models as m_models

def get(mode=None, collection=None, id=None):
    """ mode is ('list', 'item'), collection is ('band', 'event'), id if exists """
    handlers = {
        'event': c_models.Event,
        'band': c_models.Band
        }
    try:
        if mode == 'list':
            return handlers[collection].objects.all()
        else:
            return handlers[collection].objects.get(id=id)
    except (c_models.Event.DoesNotExist, c_models.Band.DoesNotExist, KeyError):
        raise Http404
 
def related(object, model):
    from django.contrib.contenttypes.models import ContentType
    content_type = ContentType.objects.get_for_model(object)
    return model.objects.filter(content_type__pk=content_type.id, object_id=object.id)
    
