from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Blog app: Site author's blog site and the authorised user can leave
    the comments on the post.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
