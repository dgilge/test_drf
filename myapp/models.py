from django.db import models

class DateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
