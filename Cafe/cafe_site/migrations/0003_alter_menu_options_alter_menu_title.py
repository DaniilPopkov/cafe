# Generated by Django 4.2 on 2024-11-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_site', '0002_alter_menu_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Салат', 'verbose_name_plural': 'Салаты'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
