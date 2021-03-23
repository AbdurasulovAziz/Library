from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User 
from django.views.generic import DetailView, ListView
from .models import Books


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DetailBook(DetailView):
    model=Books
    template_name = 'Library/book.html'
    context_object_name = 'book'
