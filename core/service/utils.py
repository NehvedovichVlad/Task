from rest_framework.permissions import IsAuthenticated
from service.models import Magazine, SoldGoods, Storage, Category


class MagazineMixin():
    queryset = Magazine.objects.all()
    permission_classes = (IsAuthenticated,)

class SoldGoodsMixin():
    queryset = SoldGoods.objects.all()
    permission_classes = (IsAuthenticated, )

class StorageMixin():
    queryset = Storage.objects.all()
    permission_classes = (IsAuthenticated, )

class CategoryMixin():
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )