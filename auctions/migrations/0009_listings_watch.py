# Generated by Django 3.2.9 on 2021-11-28 11:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20211128_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='watch',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
