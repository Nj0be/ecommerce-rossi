# Generated by Django 5.1.3 on 2024-12-02 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_date_created_order_created_at'),
        ('products', '0014_rename_date_created_product_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProduct',
            new_name='OrderItem',
        ),
    ]