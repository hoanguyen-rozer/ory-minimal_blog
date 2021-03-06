from django.urls import path

from src.views.post import post_detail_view, homepage_view
from src.views.comment import comment_add_view

app_name = 'posts'

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('<slug:slug>/', post_detail_view, name='detail'),
    path('<int:post_id>/comment/', comment_add_view, name='comment'),
]
