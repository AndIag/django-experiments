from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize
from stdimage import StdImageField


def get_image_path(instance, filename):
    return filename


class ImageKit(models.Model):
    image = models.ImageField(upload_to=get_image_path, null=True)
    thumbnail = ProcessedImageField(upload_to=get_image_path,
                                    processors=[SmartResize(200, 200)],
                                    format='JPEG',
                                    options={'quality': 70}, null=True)


class StdImage(models.Model):
    image = StdImageField(upload_to=get_image_path,
                          variations={'thumbnail': {'width': 200, 'height': 200, 'crop': True}})
