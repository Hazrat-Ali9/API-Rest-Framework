from .models import Item
from django.contrib import admin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'summery', 'seen', 'category', 'created_date','images')
    prepopulated_fields = {'slug': ('item_name',)}

admin.site.register(Item, ProductAdmin)
