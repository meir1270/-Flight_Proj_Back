# Generated by Django 3.2.8 on 2022-08-22 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20220821_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='customer',
        ),
    ]
