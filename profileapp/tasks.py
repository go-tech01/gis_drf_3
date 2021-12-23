import sys
import time
from io import BytesIO
from PIL import Image
from celery import shared_task
from django.core.files.uploadedfile import InMemoryUploadedFile


@shared_task
def generate_thumbnail_celery_lag(profile_id):
    from profileapp.models import Profile
    target_profile = Profile.objecs.get(pk=profile_id)
    time.sleep(10)
    img = Image.open(target_profile.image)
    width, height = img.size
    ratio = height /width
    pixel = min(250, width)
    img = img.convert('RGB')
    img.thumbnail((pixel, round(pixel *ratio)))
    output = BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)
    target_profile.thumb = InMemoryUploadedFile(output, "ImageField", target_profile.image.name,
                                      'image/jpeg', sys.getsizeof(output), None)
    target_profile.save()