# Generated by Django 3.2.6 on 2021-08-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20210824_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie_rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=20),
        ),
    ]
