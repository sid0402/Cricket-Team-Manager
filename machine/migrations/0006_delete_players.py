# Generated by Django 4.2.2 on 2023-06-10 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0005_trades_description_alter_trades_players_team1_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Players",
        ),
    ]
