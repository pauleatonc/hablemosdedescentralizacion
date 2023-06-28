from django.db import models
from datetime import datetime


class Countdown(models.Model):
    end_date = models.DateField()

    def get_days_left(self):
        today = datetime.now().date()
        days_left = (self.end_date - today).days
        return days_left