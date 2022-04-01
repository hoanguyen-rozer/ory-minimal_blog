from django.views.generic import TemplateView, DetailView

from src.forms import CommentForm
from src.models import Post, Comment


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context_data = super(HomepageView, self).get_context_data(**kwargs)
        context_data['latest_posts'] = Post.objects.published().select_related('category').prefetch_related(
            'tags').order_by('-published_at')
        return context_data


homepage_view = HomepageView.as_view()


class PostDetailView(DetailView):
    template_name = 'post-detail.html'
    context_object_name = 'post_detail'
    queryset = Post.objects.published().select_related('category').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        post = Post.objects.get(slug=self.kwargs.get('slug'))
        comments_on_post = Comment.objects.filter(post=post)
        context.update({
            'comments_on_post': comments_on_post,
            'comment_form': comment_form
        })
        return context


post_detail_view = PostDetailView.as_view()
