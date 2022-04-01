from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    username = models.CharField(_('username'), max_length=254)
    post = models.ForeignKey(to='src.Post', related_name='comments_on_post', on_delete=models.CASCADE)
    content = models.TextField(_('content'))
    user_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.content}"

    class Meta:
        ordering = ('created_at',)
