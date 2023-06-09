# Generated by Django 4.2 on 2023-04-16 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='AdsImage')),
                ('text', models.CharField(blank=True, max_length=255)),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('best_offer', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
                ('avatar', models.ImageField(upload_to='productImage')),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productSet', to='store.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='HotOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('is_publish', models.BooleanField(default=False)),
                ('banner', models.ImageField(upload_to='bannerImage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BestProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_publish', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.productmodel')),
            ],
        ),
    ]
