# Generated by Django 4.2.6 on 2023-11-09 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_produk_kategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='harga',
        ),
    ]
