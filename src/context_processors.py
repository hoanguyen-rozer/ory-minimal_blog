from django.db.models import Count

from src.models import Category, Tag


def access_categories_tags(request):
    """
        This context processor return list category
    """
    categories = Category.objects.annotate(number_of_posts=Count('posts'))
    tags = Tag.objects.all()
    data_access = {
        'categories': categories,
        'tags': tags
    }

    return data_access
