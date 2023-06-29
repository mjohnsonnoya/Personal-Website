from django.db import models
from django.utils import timezone
import datetime


class Feedback(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_interesting = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    display_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Feedback #{self.id}"