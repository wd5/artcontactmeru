# -*- coding: utf-8 -*-
 
def related(model_a, id, model_b):
    from django.contrib.contenttypes.models import ContentType
    try:
        object = model_a.objects.get(id=id)
    except model_a.DoesNotExist:
        return list()
    content_type = ContentType.objects.get_for_model(object)
    return model_b.objects.filter(content_type__pk=content_type.id, object_id=object.id)

def get_media(media, model, id):
    return list() \
        + [i for i in related(model, id, media.Photo) ] \
        + [i for i in related(model, id, media.Video) ] \
        + [i for i in related(model, id, media.Audio) ]
