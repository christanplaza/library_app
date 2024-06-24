from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
  books = Book.objects.all()
  name = "tantan"
  return render(request, 'library_index.html', {'name': name, 'books': books})

def book_detail(request, id):
  book = Book.objects.get(pk=id)
  return render(request, 'library_detail.html', { 'book': book })

def create(request):
  return render(request, 'library_create_book.html')

def update(request):
  return render(request, 'library_update_book.html')

def delete(request):
  return render(request, 'library_delete_book.html')

