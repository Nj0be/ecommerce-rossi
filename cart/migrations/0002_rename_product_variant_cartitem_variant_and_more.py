# Generated by Django 5.1.3 on 2024-11-18 12:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('products', '0002_alter_productvariant_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_variant',
            new_name='variant',
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('variant', 'customer')},
        ),
    ]
