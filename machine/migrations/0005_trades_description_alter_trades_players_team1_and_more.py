# Generated by Django 4.2.2 on 2023-06-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0004_trades"),
    ]

    operations = [
        migrations.AddField(
            model_name="trades",
            name="description",
            field=models.TextField(default="Description"),
        ),
        migrations.AlterField(
            model_name="trades",
            name="players_team1",
            field=models.TextField(default="players_team1"),
        ),
        migrations.AlterField(
            model_name="trades",
            name="players_team2",
            field=models.TextField(default="players_team2"),
        ),
    ]