# Generated by Django 3.2.4 on 2021-06-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optionsPF', '0019_alter_butterflyspread_strategy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='butterflyspread',
            name='collapsible_tag',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='butterflyspread',
            name='strategy_name',
            field=models.CharField(max_length=50),
        ),
    ]
