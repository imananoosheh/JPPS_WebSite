from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import content,coverImage

def facilities(request):
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    try:
        contents = content.objects.latest('id')
    except ObjectDoesNotExist:
        contents = None
    context = {
        'cover' : cover,
        'content' : contents,
    }
    
    return render(request, 'facilities.html', context)
