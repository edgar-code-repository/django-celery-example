import time
from celery.decorators import task

@task(name='expensive_computation_task')
def very_expensive_computation():
    time.sleep(30)
    return "The task has finished!!!!"
