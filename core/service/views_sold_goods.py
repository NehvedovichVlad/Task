from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from service.add_filters import SoldGoodsFilterInFilter
from service.models import SoldGoods
from service.serializers import SoldGoodsListSerializer


class SoldGoodsListView(generics.ListAPIView):
    serializer_class = SoldGoodsListSerializer
    queryset = SoldGoods.objects.all()
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = SoldGoodsFilterInFilter

class SoldGoodsCreateView(generics.CreateAPIView):
    serializer_class = SoldGoodsListSerializer
    queryset = SoldGoods.objects.all()
    permission_classes = (IsAuthenticated, )

