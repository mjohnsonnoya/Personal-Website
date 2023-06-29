from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.submit_feedback, name='submit_feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
