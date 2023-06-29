# feedback/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def thank_you(request):
    interesting_feedback = Feedback.objects.filter(is_interesting=True, display_until__gt=timezone.now()).order_by('-created_at')
    context = {
        'interesting_feedback': interesting_feedback,
    }
    return render(request, 'feedback/thank_you.html', context)

def submit_feedback(request):
    form = FeedbackForm(request.POST or None)
    interesting_feedback = Feedback.objects.filter(is_interesting=True, display_until__gt=timezone.now()).order_by('-created_at')
    context = {
        'form': form,
        'interesting_feedback': interesting_feedback,
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback:thank_you')

    return render(request, 'feedback/submit_feedback.html', context)
