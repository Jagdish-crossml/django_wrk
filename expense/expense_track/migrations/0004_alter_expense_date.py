# Generated by Django 3.2.6 on 2021-08-23 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_track', '0003_auto_20210823_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
