# -*- coding: utf-8 -*-

from django.http import Http404
from collection import models as c_models
from mediastore import models as m_models

def get(mode=None, collection=None, id=None):
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
            return model.objects.get(id=id)
    except (c_models.Event.DoesNotExist, c_models.Band.DoesNotExist, KeyError):
        raise Http404
 
def related(model_a, id, model_b):
    from django.contrib.contenttypes.models import ContentType
    try:
        object = model_a.objects.get(id=id)
    except model_a.DoesNotExist:
        return list()
    content_type = ContentType.objects.get_for_model(object)
    return model_b.objects.filter(content_type__pk=content_type.id, object_id=object.id)
    
