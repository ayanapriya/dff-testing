
from django.urls import path
from rest_framework import routers

from dff_backend.views.ping import Ping
from dff_backend.views.colections import CollectionViewset

router = routers.DefaultRouter()
router.register(r'collections', CollectionViewset,
                basename='category')
router.register(r'offers', CollectionViewset,
                basename='category')

urlpatterns = [
    path('ping/', Ping.as_view(), name='ping')
]
urlpatterns += router.urls
