from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from .models import person, category, coverImage 

def staff(request):
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    try:
        All_person = person.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_categories = None
    try:
        All_categories = category.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_categories = None
    context = {
        'cover' : cover,
        'person' : All_person,
        'categories' : All_categories
    }
    return render(request, 'staff.html', context)
