# Generated by Django 4.2.2 on 2023-06-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0012_trades_delete_trades_compensation_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trades",
            name="net_salary",
            field=models.TextField(default="0"),
        ),
    ]