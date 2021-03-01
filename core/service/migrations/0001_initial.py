# Generated by Django 3.1.7 on 2021-03-01 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=150, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazine', models.CharField(db_index=True, max_length=150, verbose_name='Наименование магазина')),
                ('goods', models.ManyToManyField(to='service.Goods')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'ordering': ['magazine'],
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.CharField(db_index=True, max_length=150, verbose_name='Склад')),
                ('goods', models.ManyToManyField(to='service.Goods')),
            ],
            options={
                'verbose_name': 'Склады',
                'verbose_name_plural': 'Склад',
                'ordering': ['storage'],
            },
        ),
        migrations.CreateModel(
            name='SoldGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.category', verbose_name='Категория')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.magazine', verbose_name='Магазин')),
                ('sold_goods', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.goods', verbose_name='Проданные Товары')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.storage', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
                'ordering': ['sold_goods'],
            },
        ),
    ]
