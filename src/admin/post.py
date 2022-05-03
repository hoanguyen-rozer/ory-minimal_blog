from django.contrib import messages, admin
from django.utils.translation import ngettext

from src.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    date_hierarchy = 'created_at'
    empty_value_display = 'Not Set'

    list_display = ('title', 'created_at', 'status', 'published_at')
    list_filter = ('category', 'status')
    list_select_related = ('category',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category',)

    @admin.action(description="Make selected posts as published")
    def make_published(self, request, queryset):
        """
        Action allow change status publish for multiple posts
        """
        updated = queryset.update(status=Post.PostStatus.PUBLISHED)
        self.message_user(request, ngettext(
            '%d post was successfully marked as published.',
            '%d posts were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    actions = (make_published,)

    fieldsets = (
        (None, {
            'fields': ('category', 'tags')
        }),
        ('Required Information', {
            'description': "These fields are required for each post.",
            'fields': ('title', 'slug', 'image', 'content', 'status')
        }),
        ('Time Information', {
            'fields': ('published_at',)
        })
    )
