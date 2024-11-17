from django.db import models
from django.utils import timezone


# Create your models here.
class Pass(models.Model):
    pass_number = models.PositiveIntegerField(
        verbose_name="Номер пропуска", null=True, blank=True
    )
    pass_type = models.CharField(
        max_length=255, verbose_name="Тип пропуска", null=True, blank=True
    )
    name = models.CharField(max_length=255, verbose_name="ФИО", null=True, blank=True)
    service = models.CharField(
        max_length=255, verbose_name="Служба", null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=255, verbose_name="Номер телефона", null=True, blank=True
    )
    car = models.CharField(
        max_length=255, verbose_name="Автомобиль", null=True, blank=True
    )
    color = models.CharField(max_length=255, verbose_name="Цвет", null=True, blank=True)
    car_number = models.CharField(
        max_length=255, verbose_name="Номер автомобиля", null=True, blank=True
    )
    epc = models.CharField(max_length=255, verbose_name="Метка", unique=True)

    class Meta:
        verbose_name = "Пропуск"
        verbose_name_plural = "Пропуска"

    def __str__(self):
        return str(self.name)


class History(models.Model):
    parking_pass = models.ForeignKey(
        Pass, on_delete=models.CASCADE, verbose_name="Номер пропуска"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Отмечено")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"


class Log(models.Model):
    epc = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
