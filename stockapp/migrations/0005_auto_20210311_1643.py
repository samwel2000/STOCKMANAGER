# Generated by Django 3.1.7 on 2021-03-11 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0004_auto_20210311_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 13, 43, 25, 773424, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 13, 43, 25, 773958, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requests',
            name='requested_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 13, 43, 25, 774487, tzinfo=utc)),
        ),
    ]
