from django.contrib import admin
from . import models


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("parking_pass", "created_at")


class PassAdmin(admin.ModelAdmin):
    list_display = ("pass_number", "name", "service", "car", "car_number")


# Register your models here.
admin.site.register(models.Pass, PassAdmin)
admin.site.register(models.Log)
admin.site.register(models.History, HistoryAdmin)
