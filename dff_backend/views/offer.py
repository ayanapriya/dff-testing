from rest_framework.viewsets import ModelViewSet

from dff_backend.models import Offer
from dff_backend.serializers.offer import OfferSerializer


class OfferViewset(ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    def get_queryset(self):
        queryset = Offer.objects.all()
        active = self.request.query_params.get('is_active')

        if active:
            queryset = queryset.filter(Offer.is_active == True)
            
        return queryset