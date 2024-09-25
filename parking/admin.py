from django.contrib import admin
from . import models


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("parking_pass", "created_at")


class PassAdmin(admin.ModelAdmin):
    list_display = ("pass_number", "name", "service", "car", "car_number", "epc")
    search_fields = ("name", "service", "epc")
    list_per_page = 20
    list_filter = ("service",)


# Register your models here.
admin.site.register(models.Pass, PassAdmin)
admin.site.register(models.Log)
admin.site.register(models.History, HistoryAdmin)
