
from rest_framework import serializers
from dff_backend.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url')

    class Meta:
        model = Offer
        fields = ['id', 'offer_percentage', 'description',
                  'image', 'collection', 'sub_category']
