# Generated by Django 4.2 on 2023-04-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=300),
        ),
    ]
