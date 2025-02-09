# Generated by Django 5.1.5 on 2025-01-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                ("year", models.IntegerField()),
                ("author", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BookList",
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
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "books",
                    models.ManyToManyField(
                        related_name="lists", to="opaalalibrary.book"
                    ),
                ),
            ],
        ),
    ]
