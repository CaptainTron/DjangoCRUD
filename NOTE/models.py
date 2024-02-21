# notes/models.py

from django.db import models

class NOTE(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)

    def __str__(self):
     return self.title
