# Generated by Django 3.2.9 on 2021-11-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20211128_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='photo_URL',
            field=models.URLField(blank=True, max_length=500, verbose_name='Photo URL (optional)'),
        ),
    ]