from pprint import pprint

from django.http import JsonResponse

from src.forms import CommentForm
from src.utils import model_to_dict


def comment_add_view(request, post_id):
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post_id = post_id
        comment.save()
        print('------------------------------------------------')
        pprint(comment.id)
    else:
        return JsonResponse(comment_form.errors)
    print('--------------------------------------------')
    comment_data = model_to_dict(comment)
    # return HttpResponse(comment_serialized, content_type='text/json')
    return JsonResponse(comment_data)
