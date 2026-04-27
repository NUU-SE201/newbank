from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    reason = models.CharField(max_length=100)
    date = models.DateTimeField()
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booked_by.username}: {self.reason} ({self.date})"
