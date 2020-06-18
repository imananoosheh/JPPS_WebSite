from django.contrib import admin
from .models import category,article,coverImage

admin.site.register(article)
admin.site.register(category)
admin.site.register(coverImage)