from django.contrib import admin
from .models import Genre,Actors,Directors,ActorsVsDirectors
# Register your models here.

admin.site.register(Genre)
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(ActorsVsDirectors)