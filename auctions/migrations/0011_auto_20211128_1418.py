# Generated by Django 3.2.9 on 2021-11-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_delete_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(blank=True, choices=[('Books', 'Books'), ('Fashion', 'Fashion'), ('Home', 'Home'), ('Tech', 'Tech'), ('Tools', 'Tools'), ('Other', 'Other')], default='Other', max_length=10, verbose_name='Category (optional)'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_URL',
            field=models.URLField(blank=True, max_length=500, verbose_name='photo_URL (optional)'),
        ),
    ]