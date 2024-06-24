from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'genre')
  search_fields = ('title', 'author', 'genre')

admin.site.register(Book, BookAdmin)
