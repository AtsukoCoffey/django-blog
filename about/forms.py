from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form to send into the view that is used the model of CollaborateRequest
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

