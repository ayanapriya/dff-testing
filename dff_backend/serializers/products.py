
from rest_framework import serializers
from dff_backend.models import Product, ProductInventory


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image', 'offer']

    def to_representation(self, value):
        pass


class ProductDetailSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField(required=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'size', 'quantity',
                  'offer', 'collection', 'sub_category']

    @staticmethod
    def get_size(size):
        size = ProductInventory.size
        return size
