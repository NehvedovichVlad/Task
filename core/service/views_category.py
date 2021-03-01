from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from service.models import Category
from service.serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    filter_backends = [SearchFilter]
    search_fields = ['category']

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )


