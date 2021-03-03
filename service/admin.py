from django.contrib import admin

from .models import Goods, Magazine, Storage, Category, SoldGoods

admin.site.register(Goods)
admin.site.register(Magazine)
admin.site.register(Storage)
admin.site.register(Category)
admin.site.register(SoldGoods)

