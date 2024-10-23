from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Register the model into admin site. Instead of admin.site.register(About)
    Use decorator @admin and class based model to use Summernote.
    """
    summernote_fields = ('content',)


# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Register the Collaborate request message model into admin site.
    Use decorator @admin and class based model to use Summernote.
    """
    list_display = ('message', 'read')
