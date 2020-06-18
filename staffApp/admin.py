from django.contrib import admin
from .models import category,person,coverImage

admin.site.register(person)
admin.site.register(category)
admin.site.register(coverImage)