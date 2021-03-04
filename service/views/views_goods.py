from rest_framework import generics
from service.serializers import GoodsDetailSerializer, GoodsListSerializer
from service.utils import GoodsMixin


class GoodsCreateView(GoodsMixin,generics.CreateAPIView):
    serializer_class = GoodsDetailSerializer

class GoodsListView(GoodsMixin, generics.ListAPIView):
    serializer_class = GoodsListSerializer

class GoodsDetailView(GoodsMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodsDetailSerializer


