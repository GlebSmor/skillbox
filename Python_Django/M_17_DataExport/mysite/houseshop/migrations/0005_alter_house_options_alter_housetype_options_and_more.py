# Generated by Django 4.0.6 on 2023-05-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseshop', '0004_delete_newsitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['pk'], 'verbose_name': 'House', 'verbose_name_plural': 'Houses'},
        ),
        migrations.AlterModelOptions(
            name='housetype',
            options={'ordering': ['pk'], 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['pk'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='roomscount',
            options={'ordering': ['pk'], 'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
    ]