from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About Page
    """
    about = About.objects.all().order_by('-created_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )