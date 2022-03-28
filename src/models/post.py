import os
from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from src.constants import DEFAULT_POST_IMAGE
from src.models import Category
from src.utils import post_image_filename


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter()


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Post(models.Model):
    class PostStatus(models.TextChoices):
        PUBLISHED = 'P', _('Published')
        DRAFT = 'D', _('Draft')

    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to=post_image_filename, blank=True, null=True)
    content = RichTextField(_('Content'))
    tags = models.ManyToManyField(to='src.Tag', related_name='posts')
    status = models.CharField(
        _('Status'), choices=PostStatus.choices, max_length=1, default=PostStatus.DRAFT)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    published_at = models.DateTimeField(
        _('Published at'), null=True, blank=True)

    objects = PostManager()

    error_messages = {
        'invalid': 'Draft entries may not have a publication date.'
    }

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'slug': self.slug})

    def clean(self):
        if self.status == self.PostStatus.DRAFT and self.published_at is not None:
            raise ValidationError(
                message=self.error_messages['invalid'],
                code='invalid'
            )
        if self.status == self.PostStatus.PUBLISHED and self.published_at is None:
            self.published_at = datetime.now()

    def get_image(self):
        return self.image if self.image else DEFAULT_POST_IMAGE
