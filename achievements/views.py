from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import achievement,coverImage


def achievements(request):
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    try:
        All_achievement = achievement.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_achievement = None
    context = {
        'achievements' : All_achievement,
        'cover' : cover,
    }
    return render(request, 'achievements.html', context)
