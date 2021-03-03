from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        get_latest_by = ['name']


class Category(models.Model):
    category = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category']


class Storage(models.Model):
    storage = models.CharField(max_length=150, db_index=True, verbose_name='Склад')
    goods = models.ManyToManyField(Goods)

    def __str__(self):
        return self.storage

    class Meta:
        verbose_name = 'Склады'
        verbose_name_plural = 'Склад'
        ordering = ['storage']


class Magazine(models.Model):
    magazine = models.CharField(max_length=150, db_index=True, verbose_name='Наименование магазина')
    goods = models.ManyToManyField(Goods)

    def __str__(self):
        return self.magazine

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['magazine']


class SoldGoods(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.PROTECT, verbose_name='Товар', null=True)
    magazine = models.ForeignKey('Magazine', on_delete=models.PROTECT, verbose_name='Магазин')
    storage = models.ForeignKey('Storage', on_delete=models.PROTECT, verbose_name='Склад')

    class Meta:
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'
        ordering = ['goods']
