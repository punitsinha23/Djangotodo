from django import forms
from .models import todo

class todoform(forms.ModelForm):
    class Meta:
        model = todo  # Link the form to the todo model
        fields = ['title', 'desc', 'due_date']  # Specify the fields to include in the form
