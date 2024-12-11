from django.shortcuts import render
from . models import Books

# Create your views here.
def show_books(request):
    books = Books.objects.all()
    return render(request, 'books/books.html', {'books': books})