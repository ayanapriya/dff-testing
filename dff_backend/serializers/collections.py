
from rest_framework import serializers
from dff_backend.models import Category, ProductInventory


class CollectionSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url')

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']
