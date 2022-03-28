from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name of category'), max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(_('Description'), max_length=255)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('name',)

    def __str__(self) -> str:
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={'slug': self.slug})
