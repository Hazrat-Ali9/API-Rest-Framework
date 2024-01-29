from rest_framework import serializers
from .models import Item

class DataStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'summery', 'images', 'seen', 'slug','category']