from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from service.models import Storage
from service.serializers import StorageDetailSerializer, StorageListSerializer


class StorageCreateView(generics.CreateAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()
    permission_classes = (IsAuthenticated, )

class StorageListView(generics.ListAPIView):
    # get a list of storage with free goods
    serializer_class = StorageListSerializer
    queryset = Storage.objects.all()
    #    queryset = Storage.objects.filter(goods__sold=True)
    permission_classes = (IsAuthenticated, )
    filter_backends = [SearchFilter]
    search_fields = ['storage']

class StorageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()
    permission_classes = (IsAuthenticated, )



