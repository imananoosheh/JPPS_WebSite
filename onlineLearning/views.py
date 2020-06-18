from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import content,coverImage
def onlineLearning(request):
    try:
        contents = content.objects.latest('id')
    except:
        contents = None
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    context = {
        'content' : contents,
    }
    
    return render(request, 'onlinelearning.html', context)
