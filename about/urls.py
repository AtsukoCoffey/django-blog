from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),   # Use as {% url 'about' %} from template
]