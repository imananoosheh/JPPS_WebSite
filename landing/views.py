from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from .models import sections,relatedWebsites,landingVideo,coverImage
from newsApp.models import article,category

def Home(request):
    try:
        All_Sections = sections.objects.all()
    except ObjectDoesNotExist:
        All_Sections = None
    try:
        All_articles = article.objects.all().order_by('-id')[:3]
    except ObjectDoesNotExist:
        All_articles = None
    try:
        All_categories = category.objects.all()
    except ObjectDoesNotExist:
        All_categories = None
    try:
        All_relatedWebsites = relatedWebsites.objects.all()
    except ObjectDoesNotExist:
        All_relatedWebsites = None
    try:
        All_Videos = landingVideo.objects.all()
    except ObjectDoesNotExist:
        All_Videos= None
    context = {
        'sections' : All_Sections,
        'categories' : All_categories,
        'articles' : All_articles,
        'websites' : All_relatedWebsites,
        'vidsPics' : All_Videos
    }
    
    return render(request, 'index.html', context)
