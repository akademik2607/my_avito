# Generated by Django 4.1.3 on 2022-11-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_remove_advertisement_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(blank=True, to='ads.location', verbose_name='Локация'),
        ),
    ]
