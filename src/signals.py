from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from src.models import Post
from src.utils import unique_slug_generator

User = get_user_model()


@receiver(pre_save, sender=Post)
def create_slug(sender, instance, **kwargs):
    instance.slug = unique_slug_generator(instance)
