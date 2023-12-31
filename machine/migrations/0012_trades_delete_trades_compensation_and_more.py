# Generated by Django 4.2.2 on 2023-06-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0011_trades_compensation_title_trades_players_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trades",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team1", models.CharField(max_length=500)),
                ("team2", models.CharField(max_length=500)),
                ("trade_type", models.TextField(default="Player")),
                ("players_team1", models.TextField(default="players_team1", null=True)),
                (
                    "players_team2",
                    models.TextField(blank=True, default="players_team2", null=True),
                ),
                (
                    "compensation",
                    models.TextField(blank=True, default="0.1", null=True),
                ),
                ("description", models.TextField(default="Description")),
                ("title", models.TextField(default="Description")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Trades_Compensation",
        ),
        migrations.DeleteModel(
            name="Trades_Players",
        ),
    ]
