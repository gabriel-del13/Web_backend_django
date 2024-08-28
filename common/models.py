from django.db import models

class BaseItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True