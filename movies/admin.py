from django.contrib import admin

from . import models

# Register your models here.


admin.site.register(models.Genre)
admin.site.register(models.Actor)
admin.site.register(models.Character)
admin.site.register(models.Movie)
