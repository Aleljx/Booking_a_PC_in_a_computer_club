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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" #{self.user.username} #{self.computer}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['start_time']

class Equipment(models.Model):
    pass