from django.db import models
from core.models import AbstractTimestampField


class PowerStation(AbstractTimestampField):
    name = models.CharField(max_length=50)
    voltage = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.voltage}) station"

