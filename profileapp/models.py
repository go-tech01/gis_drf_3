import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    thumb = models.ImageField(upload_to='profile/thumbnail', null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.generate_thumbnail()
        super().save(*args, **kwargs)

    def generate_thumbnail(self):
        img = Image.open(self.image)
        width, height = img.size
        ratio = height / width
        pixel = min(250, width)
        img = img.convert('RGB')
        img.thumbnail((pixel, round(pixel*ratio)))
        output = BytesIO()
        img.save(output, format='JPEG', quality=95)
        output.seek(0)
        self.thumb = InMemoryUploadedFile(output, "ImageField", self.image.name,
                                          'image/jpeg', sys.getsizeof(output), None)