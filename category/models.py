from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=255,blank=True)
    category_image = models.ImageField(upload_to='photos/categories',blank=True)