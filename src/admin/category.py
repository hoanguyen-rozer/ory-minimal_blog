from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from src.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_post', 'view_posts_link')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def number_post(self, obj):
        # result = Post.objects.filter(category=obj).count()
        result = obj.posts.count()
        return format_html("<b>{}</b>", result)

    number_post.short_description = 'Number of post'

    def view_posts_link(self, obj):
        count = obj.posts.count()
        url = reverse('admin:posts_post_changelist') + '?' + urlencode({'category__id': f"{obj.id}"})
        return format_html('<a href="{}">{} Posts</a>', url, count)

    view_posts_link.short_description = 'Posts'
