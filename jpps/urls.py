
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^ckeditor/upload/', include('ckeditor_uploader.urls')),
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #url(r'jet/', include('jet.urls')),
    url(r'admin/', admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^Gallery/', include('galleryApp.urls', namespace='galleries')),
    url(r'^news/',include('newsApp.urls', namespace='news')),
    url(r'^staff/',include('staffApp.urls')),
    url(r'^facilities/',include('facilities.urls')),
    url(r'^achievements/',include('achievements.urls')),
    url(r'^registration/',include('registration.urls')),
    url(r'^vision/',include('vision.urls')),
    url(r'^contactus/',include('contactUs.urls')),
    url(r'^onlinelearning/',include('onlineLearning.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)