# Generated by Django 3.1.7 on 2021-03-11 05:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 5, 0, 6, 999450, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requests',
            name='requested_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 11, 5, 0, 7, 4422, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_date', models.DateField(default=datetime.datetime(2021, 3, 11, 5, 0, 6, 999450, tzinfo=utc))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stockapp.product')),
            ],
            options={
                'verbose_name_plural': 'Products added',
            },
        ),
    ]
