from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from . import models


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("parking_pass", "get_car", "get_car_number", "created_at")
    search_fields = (
        "parking_pass__car",
        "parking_pass__car_number",
        "parking_pass__name",
        "created_at",
    )

    @admin.display(description="Номер автомобиля")
    def get_car_number(self, obj):
        return obj.parking_pass.car_number

    @admin.display(description="Автомобиль")
    def get_car(self, obj):
        return obj.parking_pass.car


class HistoryFormSet(BaseInlineFormSet):
    def get_queryset(self):
        qs = super(HistoryFormSet, self).get_queryset()
        return qs[:20]


class HistoryInline(admin.TabularInline):
    model = models.History
    formset = HistoryFormSet
    fields = [
        "created_at",
    ]
    ordering = ("-created_at",)
    readonly_fields = [
        "created_at",
    ]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = False


class PassAdmin(admin.ModelAdmin):
    list_display = ("pass_number", "name", "service", "car", "car_number", "epc")
    search_fields = ("name", "service", "epc")
    list_per_page = 20
    list_filter = ("service",)
    list_display_links = ("name",)
    inlines = [HistoryInline]


# Register your models here.
admin.site.register(models.Pass, PassAdmin)
admin.site.register(models.Log)
admin.site.register(models.History, HistoryAdmin)
