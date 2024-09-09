from django.urls import path
from . import views

# All URLS after 'library/<urls here>'
urlpatterns = [
  path('books', views.index, name='index'),
  path('books/<id>/', views.book_detail, name='book-detail'),
  path('books/create', views.create, name='create-book'),
  path('update-book', views.update, name='update-book'),
  path('delete-book', views.delete, name='delete-book'),
]
