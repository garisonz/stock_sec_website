# Generated by Django 5.0 on 2024-01-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0003_stock_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_info',
            old_name='cik_number',
            new_name='cik_str',
        ),
        migrations.RenameField(
            model_name='stock_info',
            old_name='ticker_symbol',
            new_name='ticker',
        ),
        migrations.RenameField(
            model_name='stock_info',
            old_name='company_name',
            new_name='title',
        ),
    ]