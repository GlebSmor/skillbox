# Generated by Django 4.2 on 2023-04-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_created_at_product_discount_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
