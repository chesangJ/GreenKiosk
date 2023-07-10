# Generated by Django 4.2.3 on 2023-07-10 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_rename_user_customer_user_id'),
        ('orders', '0005_orders_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
