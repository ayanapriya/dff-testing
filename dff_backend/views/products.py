from rest_framework import viewsets
from dff_backend.models import Product
from dff_backend.serializers.products import ProductListSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailSerializer
