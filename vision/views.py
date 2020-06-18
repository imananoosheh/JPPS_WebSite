from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import content,coverImage
def vision(request):
    try:
        contents = content.objects.latest('id')
    except ObjectDoesNotExist:
        contents = None
    try:
        cover = coverImage.objects.all().order_by('id')[0]
    except:
        cover = None
    context = {
        'cover' : cover,
        'content' : contents,
    }
    
    return render(request, 'vision.html', context)
