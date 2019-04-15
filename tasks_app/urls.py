from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.example_call, name='example_call'),
    path('call_celery_task', views.call_celery_task, name='call_celery_task')
]