# Generated by Django 4.2.2 on 2023-06-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0009_trades_compensation_rename_trades_trades_players"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trades_compensation",
            name="compensation",
            field=models.TextField(default="0.1"),
        ),
    ]