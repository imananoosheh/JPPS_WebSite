from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import galleryCategory, Gallery, coverImage


def gallery_detail(request, slug=None):
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    try:
        instance = get_object_or_404(Gallery, slug=slug)
    except ObjectDoesNotExist:
        instance = None
    context = {
        'cover' : cover,
        'Gal' : instance
    }
    return render(request, 'singlepagegallery.html', context)

def All(request):
    try:
        cover = coverImage.objects.latest('id')
    except ObjectDoesNotExist:
        cover = None
    try:
        All_categories = galleryCategory.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_categories = None
    try:
        All_galleries = Gallery.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_galleries = None
    context = {
        'cover' : cover,
        'galleries' : All_galleries,
        'categories' : All_categories
    }
    return render(request, 'gallery.html', context)
