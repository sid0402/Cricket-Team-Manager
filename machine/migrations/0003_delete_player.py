# Generated by Django 4.2.2 on 2023-06-08 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0002_player"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Player",
        ),
    ]
