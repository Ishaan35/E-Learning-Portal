# Generated by Django 3.2.5 on 2021-08-08 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationPortal', '0002_auto_20210807_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 51, 51, 713239)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 51, 51, 713239)),
        ),
        migrations.AlterField(
            model_name='quizsubmission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 20, 51, 51, 719256)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 20, 51, 51, 716231)),
        ),
        migrations.AlterField(
            model_name='text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 51, 51, 714237)),
        ),
    ]