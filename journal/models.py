from django.db import models
from django.utils import timezone


class Entry(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.create_date + ' Entry'
