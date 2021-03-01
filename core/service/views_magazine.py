from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from service.models import Magazine
from service.serializers import MagazineDetailSerializer, MagazineListSerializer


class MagazineCreateView(generics.CreateAPIView):
    serializer_class = MagazineDetailSerializer
    queryset = Magazine.objects.all()
    permission_classes = (IsAuthenticated, )


class MagazineListView(generics.ListAPIView):
    serializer_class = MagazineListSerializer
    queryset = Magazine.objects.all()
    permission_classes = (IsAuthenticated, )
    filter_backends = [SearchFilter]
    search_fields = ['magazine']

class MagazineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MagazineDetailSerializer
    queryset = Magazine.objects.all()
    permission_classes = (IsAuthenticated, )


