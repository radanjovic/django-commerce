# Generated by Django 3.2.9 on 2021-11-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name=''),
        ),
    ]