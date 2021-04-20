from django.contrib import admin
from . import models

@admin.register(models.diaryModel)
class diaryAdmin(admin.ModelAdmin):
    list_display = ("user", )


@admin.register(models.todoModel)
class todoAdmin(admin.ModelAdmin):
    list_display = ("user", "start_date")