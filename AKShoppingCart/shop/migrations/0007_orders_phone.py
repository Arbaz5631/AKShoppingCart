# Generated by Django 2.1.15 on 2020-07-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
    ]
