from django.shortcuts import render, redirect
from .models import Books
from .forms import RegistrationForm

# Create your views here.

def home(request):
    books = Books.objects.order_by('-id')
    return render(request, 'Library/Library.html', {'books':books})

def registration(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegistrationForm()
    return render(response, 'account/registration.html', {'form':form})