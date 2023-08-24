from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length = 255)

    # Changes the plural name on the admin panel to something you can define (ex. 'Categorys' > 'Categories')
    class Meta:

        ordering = ("name",)
        verbose_name_plural = "Categories"

    # Chasnges the entry name from default to actual name of entry (ex. 'Category object {x}' > '{Category name}')
    def __str__(self):
        return self.name
    
class Item(models.Model):

    category = models.ForeignKey(Category, related_name = 'items', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'item_images', blank = True, null = True)
    price = models.FloatField()
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, related_name = 'items', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name