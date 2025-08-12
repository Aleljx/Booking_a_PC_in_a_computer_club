from django.db import models
from django.contrib.auth.models import User

class Computer(models.Model):
    number = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f"Computer #{self.number}"

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"
        ordering = ['number']

class Booking(models.Model):
    pass

class Equipment(models.Model):
    pass