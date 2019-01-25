from django.contrib import admin

from . import models

admin.site.Register(models.Crossword)
admin.site.Register(models.Square)
