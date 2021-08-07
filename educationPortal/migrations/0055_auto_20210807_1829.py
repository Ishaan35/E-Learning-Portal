# Generated by Django 3.2.5 on 2021-08-07 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationPortal', '0054_auto_20210807_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 18, 29, 44, 697808)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 18, 29, 44, 697808)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='lastInteracted',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quizsubmission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 18, 29, 44, 705880)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 18, 29, 44, 701803)),
        ),
        migrations.AlterField(
            model_name='text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 18, 29, 44, 697808)),
        ),
    ]
