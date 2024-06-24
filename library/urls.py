from django.urls import path
from . import views

# All URLS after 'library/<urls here>'
urlpatterns = [
  path('books', views.index, name='index'),
  path('create-book', views.create, name='create-book'),
  # Create Book
  # Update Book
  path('update-book', views.update, name='update-book'),
  # Delete Book
  path('delete-book', views.delete, name='delete-book'),
]
