# from main import celery
from celery import shared_task


@shared_task
def add(x, y):
    print(" RUN SCHEDULE TASK")
    return x + y
