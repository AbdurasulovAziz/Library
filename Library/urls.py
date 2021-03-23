from django.urls import path, include
from . import views
from . import forms

urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:pk>' , forms.DetailBook.as_view(), name='book'),
    path('registration', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
]
