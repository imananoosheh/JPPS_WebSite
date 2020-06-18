
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$',views.All, name = "All"),
    url(r'(?P<slug>[-\w]+)/$',views.gallery_detail, name = "detail"),
    
    #include('djadmin.urls')),

]
