from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    likes = models.IntegerField()
    user_email = models.EmailField()

