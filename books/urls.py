from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_books, name='show_books_reverse')
]
