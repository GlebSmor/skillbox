# Generated by Django 4.0.6 on 2023-05-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='housetype',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='roomscount',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default='House', max_length=100),
        ),
    ]
