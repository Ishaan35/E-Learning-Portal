# Generated by Django 3.2.5 on 2021-07-31 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationPortal', '0029_auto_20210731_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 17, 48, 27, 680598)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='lastInteracted',
            field=models.FloatField(),
        ),
    ]
