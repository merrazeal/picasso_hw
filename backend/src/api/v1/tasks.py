import time
from celery import shared_task

from files.models import File


@shared_task
def render_file(file_id):
    file = File.objects.get(id=file_id)
    time.sleep(5)  # render file ...
    file.processed = True
    file.save()
