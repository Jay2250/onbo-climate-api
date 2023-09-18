
from django.db import models
import uuid

class ClimateRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    climate = models.CharField(max_length=10, choices=[('hot', 'Hot'), ('humid', 'Humid'), ('rainy', 'Rainy'), ('cold', 'Cold')])
    area_code = models.PositiveIntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    chances_of_rain = models.FloatField()
