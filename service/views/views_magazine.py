from rest_framework import generics
from rest_framework.filters import SearchFilter
from service.serializers import MagazineDetailSerializer, MagazineListSerializer
from service.utils import MagazineMixin


class MagazineCreateView(MagazineMixin, generics.CreateAPIView):
    serializer_class = MagazineDetailSerializer

class MagazineListView(MagazineMixin, generics.ListAPIView):
    serializer_class = MagazineListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['magazine']

class MagazineDetailView(MagazineMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MagazineDetailSerializer



