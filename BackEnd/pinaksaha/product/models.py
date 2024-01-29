from django.db import models

from category.models import Category
from django.urls import reverse

class Item(models.Model):
    item_name = models.CharField(max_length=100,unique = True)
    slug = models.SlugField(max_length=100,unique = True)
    summery = models.CharField(max_length=400,blank = True)
    seen = models.CharField(max_length=100,unique = True)
    images = models.ImageField(upload_to='photos/products',blank=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self.item_name
