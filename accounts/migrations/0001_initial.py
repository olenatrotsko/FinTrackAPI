# Generated by Django 5.0.6 on 2024-06-29 18:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], max_length=3)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_main', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]