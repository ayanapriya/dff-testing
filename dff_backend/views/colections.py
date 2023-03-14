from rest_framework.viewsets import ModelViewSet

from dff_backend.models import Collection
from dff_backend.serializers.collections import CollectionSerializer


class CollectionViewset(ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
