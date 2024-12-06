# Generated by Django 5.1.3 on 2024-12-06 10:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_product_variant_cartitem_variant_and_more'),
        ('products', '0015_alter_brand_options_alter_color_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='customer',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('variant', 'user')},
        ),
    ]