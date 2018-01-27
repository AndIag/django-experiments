from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from imageExperiment.models import ImageKit, StdImage

_UNSAVED = 'unsaved_image'


@receiver(pre_save, sender=ImageKit)
@receiver(pre_save, sender=StdImage)
def skip_saving_file(sender, instance, **kwargs):
    """
    Skips image saving until instance creation
    """
    if not instance.id and not hasattr(instance, _UNSAVED):
        if hasattr(instance, "image") and instance.image is not None:
            setattr(instance, _UNSAVED, instance.image)
            instance.image = None


@receiver(post_save, sender=ImageKit)
@receiver(post_save, sender=StdImage)
def save_file(sender, instance, created, **kwargs):
    """
    Saves delayed image
    """
    if created and hasattr(instance, _UNSAVED):
        if hasattr(instance, "image"):
            instance.image = getattr(instance, _UNSAVED)
        instance.save()
        instance.__dict__.pop(_UNSAVED)
