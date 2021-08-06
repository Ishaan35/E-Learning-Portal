# Generated by Django 3.2.5 on 2021-08-05 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationPortal', '0052_auto_20210805_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 15, 7, 9, 194566)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 15, 7, 9, 190569)),
        ),
        migrations.AlterField(
            model_name='quizsubmission',
            name='answers',
            field=models.ManyToManyField(blank=True, to='educationPortal.MCanswer'),
        ),
        migrations.AlterField(
            model_name='quizsubmission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 15, 7, 9, 198559)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 15, 7, 9, 198559)),
        ),
        migrations.AlterField(
            model_name='text',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 15, 7, 9, 194566)),
        ),
    ]
