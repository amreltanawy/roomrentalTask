# Generated by Django 4.2.5 on 2023-09-18 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Active"), (2, "Inactive")], db_index=True, default=1
                    ),
                ),
                ("reservation_price", models.DecimalField(decimal_places=2, max_digits=100)),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("meta", models.JSONField(default=dict)),
                ("room", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rooms.room")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]