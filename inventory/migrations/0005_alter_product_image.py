# Generated by Django 3.2.12 on 2023-08-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
