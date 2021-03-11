# Generated by Django 3.1.7 on 2021-03-11 05:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0002_auto_20210311_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requests',
            options={'verbose_name_plural': 'Requests'},
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='name',
            new_name='item_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 5, 11, 30, 173074, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 5, 11, 30, 173074, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requests',
            name='requested_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 5, 11, 30, 178111, tzinfo=utc)),
        ),
    ]