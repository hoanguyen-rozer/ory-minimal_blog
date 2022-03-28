import datetime
import os.path
import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """

    :param instance: instance of model which need a unique slug.
    :param new_slug: new slug for instance
    :return: str: new unique slug
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    check_slug_exists = Klass.objects.filter(slug=slug).exists()
    if check_slug_exists:
        new_slug = "{slug}-{rands}".format(slug=slug,
                                           rands=random_string_generator(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def filename_generator(filename, path=None):
    """
    Generate upload filename
    :param path: location which store file
    :param filename:
    :return: str: normalized filename
    """
    ext = filename.split('.')[-1]
    filename = "%{d}_%{rands}.%{ext}".format(d=datetime.date.today().strftime(
        "%Y%m%d"), rands=random_string_generator(), ext=ext)
    if path is None:
        path = 'images'
    return os.path.join(path, filename)


def post_image_filename(instance, filename):
    return filename_generator(filename, path='images/posts')


def user_avatar_filename(instance, filename):
    return filename_generator(filename, path='images/avatars')
