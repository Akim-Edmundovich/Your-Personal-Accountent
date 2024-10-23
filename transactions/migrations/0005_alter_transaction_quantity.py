# Generated by Django 5.1.1 on 2024-10-23 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_transaction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]