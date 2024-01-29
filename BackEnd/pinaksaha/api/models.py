from django.db import models

# Create your models here.

class DataStoreModel(models.Model):
    CATEGORY = (
    ('Books', 'Books'),
    ('Magazine', 'Magazine'),
    ('Movie', 'Movie'),
    )
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=100,unique = True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    category = models.CharField(max_length=30, choices=CATEGORY)
    seen = models.CharField(max_length=100)
