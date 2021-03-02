from rest_framework import generics
from rest_framework.filters import SearchFilter

from service.serializers import StorageDetailSerializer, StorageListSerializer
from service.utils import StorageMixin


class StorageCreateView(StorageMixin, generics.CreateAPIView):
    serializer_class = StorageDetailSerializer

class StorageListView(StorageMixin, generics.ListAPIView):
    serializer_class = StorageListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['storage']

class StorageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorageDetailSerializer




