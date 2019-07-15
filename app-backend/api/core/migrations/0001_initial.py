# Generated by Django 2.2.3 on 2019-07-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('product_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('gender', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=40)),
                ('product_description', models.TextField(blank=True)),
                ('image_urls', models.URLField(blank=True)),
                ('product_imgs_src', models.URLField(blank=True)),
                ('source', models.URLField(blank=True)),
                ('product_categories', models.CharField(max_length=40)),
                ('product_categories_mapped', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product_title', models.CharField(max_length=125)),
            ],
        ),
    ]
