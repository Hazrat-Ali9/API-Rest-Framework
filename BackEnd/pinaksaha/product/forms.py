# forms.py
from django import forms
from .models import Item

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'slug', 'summery', 'seen', 'images', 'category']
