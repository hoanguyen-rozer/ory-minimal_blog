from django.contrib import admin

from src.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions_on_bottom = True

    list_display = ('username', 'content', 'post', 'created_at')
    list_filter = ('post',)
    list_select_related = ('post',)
    search_fields = ('post',)
    list_display_links = ('content', 'post')
