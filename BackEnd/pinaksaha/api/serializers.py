from rest_framework import serializers
from .models import DataStoreModel

class DataStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStoreModel
        fields = '__all__'