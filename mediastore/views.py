# -*- coding: utf-8 -*-

from django.http import Http404

from snippets import save_file

from mediastore import models

def get(mode=None, collection=None, slug=None):
    """ mode is ('list', 'item'), collection is ('photo', 'video', audio), slug if exists """
    handlers = {
        'photo': models.Photo,
        'video': models.Video,
        'audio': models.Audio
        }
    try:
        if mode == 'list':
            return handlers[collection].objects.all()
        else:
            return handlers[collection].objects.get(slug=slug)
    except (models.Photo.DoesNotExist, models.Video.DoesNotExist, models.Audio.DoesNotExist, KeyError):
        raise Http404

@save_file('audio/mpeg')
def download_audio(request, slug):
    audio = models.Audio.objects.get(slug=slug)
    data = open(audio.file.path).read()
    return ('%s.mp3' % audio.slug, data)
    
