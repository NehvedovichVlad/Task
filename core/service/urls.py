from django.urls import path

from service.views_category import *
from service.views_goods import *
from service.views_magazine import *
from service.views_sold_goods import SoldGoodsListView, SoldGoodsCreateView
from service.views_storage import *

app_name = 'service'
urlpatterns = [
    path('goods/create/', GoodsCreateView.as_view()),
    path('goods/all/', GoodsListView.as_view()),
    path('goods/detail/<int:pk>/', GoodsDetailView.as_view()),

    path('category/create/', CategoryCreateView.as_view()),
    path('category/all/', CategoryListView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view()),

    path('magazine/create/', MagazineCreateView.as_view()),
    path('magazine/all/', MagazineListView.as_view()),
    path('magazine/detail/<int:pk>/', MagazineDetailView.as_view()),

    path('storage/create/', StorageCreateView.as_view()),
    path('storage/all/', StorageListView.as_view()),
    path('storage/detail/<int:pk>/', StorageDetailView.as_view()),

    path('sold_goods/all/', SoldGoodsListView.as_view()),
    path('sold_goods/create/', SoldGoodsCreateView.as_view()),

]
