# Generated by Django 3.2.5 on 2021-08-05 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationPortal', '0050_auto_20210804_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizsubmission',
            name='questions',
        ),
        migrations.AddField(
            model_name='quizsubmission',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 7, 50, 46, 858109)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 7, 50, 46, 858109)),
        ),
        migrations.AlterField(
            model_name='quizsubmission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 7, 50, 46, 866105)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 7, 50, 46, 862105)),
        ),
        migrations.AlterField(
            model_name='text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 7, 50, 46, 858109)),
        ),
    ]
