from django_filters import rest_framework as filters
from service.models import SoldGoods


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SoldGoodsFilterInFilter(filters.FilterSet):
    # filter in sold goods by category, goods, magazine and storage
    magazine = CharFilterInFilter(field_name='magazine__magazine', lookup_expr='in')
    storage = CharFilterInFilter(field_name='storage__storage', lookup_expr='in')
    goods = CharFilterInFilter(field_name='goods__goods', lookup_expr='in')
    category = CharFilterInFilter(field_name='goods__category', lookup_expr='in')


    class Meta:
        model = SoldGoods
        fields = '__all__'


