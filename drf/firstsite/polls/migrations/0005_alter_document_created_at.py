# Generated by Django 3.2.6 on 2021-08-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210831_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]