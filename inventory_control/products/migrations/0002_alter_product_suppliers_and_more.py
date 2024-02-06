# Generated by Django 5.0.1 on 2024-01-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(blank=True, through='products.SupplierProduct', to='suppliers.supplier'),
        ),
        migrations.AlterUniqueTogether(
            name='supplierproduct',
            unique_together={('supplier', 'product')},
        ),
    ]