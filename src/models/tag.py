from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return self.name
