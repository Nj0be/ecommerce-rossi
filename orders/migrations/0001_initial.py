# Generated by Django 5.1.3 on 2024-12-09 18:17

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40, verbose_name='Nome completo (nome e cognome)')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IT', verbose_name='Numero di telefono')),
                ('address_line_one', models.CharField(max_length=40, verbose_name='Riga Indirizzo 1')),
                ('address_line_two', models.CharField(blank=True, max_length=40, null=True, verbose_name='Riga Indirizzo 2')),
                ('postal_code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'CAP non valido, inserisci 5 numeri')], verbose_name='CAP')),
                ('city', models.CharField(max_length=40, verbose_name='city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.paymentmethod')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.province')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('order', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('variant', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='products.productvariant')),
            ],
        ),
    ]
