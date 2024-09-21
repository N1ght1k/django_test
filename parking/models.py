from django.db import models
from django.utils import timezone


# Create your models here.
class Pass(models.Model):
    pass_number = models.PositiveIntegerField()
    pass_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    epc = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pass_number)


class History(models.Model):
    parking_pass = models.ForeignKey(Pass, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Log(models.Model):
    epc = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
