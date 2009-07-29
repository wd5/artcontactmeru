import os, Image
from thumbnail import thumbnail as thumbfunc

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def thumbnail(original_image_path, arg):
    if not original_image_path:  
        return ''  

    miniature_url = thumbfunc(settings.MEDIA_URL, original_image_path, arg)
    return miniature_url  
