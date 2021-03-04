from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from service.add_filters import SoldGoodsFilterInFilter
from service.serializers import SoldGoodsListSerializer
from service.utils import SoldGoodsMixin


class SoldGoodsListView(SoldGoodsMixin, generics.ListAPIView):
    serializer_class = SoldGoodsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SoldGoodsFilterInFilter

class SoldGoodsCreateView(SoldGoodsMixin, generics.CreateAPIView):
    serializer_class = SoldGoodsListSerializer




