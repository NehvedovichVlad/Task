from rest_framework import serializers
from .models import Goods, Category, Magazine, Storage, SoldGoods


# Goods Serializers ---------------------------------------
class GoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class GoodsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'


# Category Serializers ---------------------------------------
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Magazine Serializers ---------------------------------------
class MagazineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class MagazineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

# Storage Serializers ---------------------------------------
class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class StorageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


# Sold_goods Serializers ---------------------------------------
class SoldGoodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldGoods
        fields = '__all__'

class SoldGoodsDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SoldGoods
        fields = '__all__'