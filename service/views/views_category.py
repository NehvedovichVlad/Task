from rest_framework import generics
from rest_framework.filters import SearchFilter
from service.serializers import CategoryListSerializer, CategoryDetailSerializer
from service.utils import CategoryMixin


class CategoryCreateView(CategoryMixin, generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer

class CategoryListView(CategoryMixin, generics.ListAPIView):
    serializer_class = CategoryListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['category']

class CategoryDetailView(CategoryMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer



