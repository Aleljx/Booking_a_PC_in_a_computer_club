from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    likes = models.IntegerField()
    user_email = models.EmailField()

    def __str__(self):
        return self.title

class Meta:
    ordering = ['created_at']
    db_table = 'testing_posts'
    verbose_name = 'Blog Post'
    verbose_name_plural = 'Blog Posts'
    unique_together = (('title', 'user_email'),)
    index_together = [['title', 'user_email'], ]
