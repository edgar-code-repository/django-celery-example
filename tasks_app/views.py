from django.shortcuts import render
from .tasks import very_expensive_computation


def example_call(request):
    return render(request, 'example_call.html')


def call_celery_task(request):
    task_reference = very_expensive_computation.delay()
    context = {'task_id': task_reference.id}

    return render(request, 'response.html', context)

