from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=50)
  pages = models.IntegerField()
  is_hard_bound = models.BooleanField(default=True)
  cover_image = models.URLField(default="")
