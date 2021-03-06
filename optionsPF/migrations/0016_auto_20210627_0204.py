# Generated by Django 3.2.4 on 2021-06-27 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optionsPF', '0015_rename_contract_price_butterflyspread_strategy_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='butterflyspread',
            old_name='lower_contract_price',
            new_name='high_strike_contract_price',
        ),
        migrations.RenameField(
            model_name='butterflyspread',
            old_name='midpoint_contract_price',
            new_name='low_strike_contract_price',
        ),
        migrations.RenameField(
            model_name='butterflyspread',
            old_name='upper_contract_price',
            new_name='mid_strike_contract_price',
        ),
    ]
