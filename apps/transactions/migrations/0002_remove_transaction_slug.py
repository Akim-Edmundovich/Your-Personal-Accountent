# Generated by Django 5.1.1 on 2024-11-20 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='slug',
        ),
    ]