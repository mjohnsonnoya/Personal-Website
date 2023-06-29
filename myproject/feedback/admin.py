# feedback/admin.py

from django.contrib import admin
from django.utils import timezone
import datetime
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'is_interesting')
    list_filter = ('is_interesting',)
    search_fields = ('content',)
    readonly_fields = ('id', 'created_at')
    fields = ('content', 'is_interesting', 'display_until')
    def save_model(self, request, obj, form, change):
            if obj.display_until is None and obj.is_interesting:
                obj.display_until = timezone.now() + datetime.timedelta(days=7)  # Or whatever period you choose
            super().save_model(request, obj, form, change)