# Generated by Django 4.2.2 on 2023-06-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_product_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
