from rest_framework import generics

from service.models import Goods
from service.serializers import GoodsDetailSerializer, GoodsListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class GoodsCreateView(generics.CreateAPIView):
    serializer_class = GoodsDetailSerializer
    queryset = Goods.objects.all()
    permission_classes = (IsAuthenticated, )

class GoodsListView(generics.ListAPIView):
    serializer_class = GoodsListSerializer
    queryset = Goods.objects.all()
    permission_classes = (IsAuthenticated, )

class GoodsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodsDetailSerializer
    queryset = Goods.objects.all()
    permission_classes = (IsAuthenticated, )

