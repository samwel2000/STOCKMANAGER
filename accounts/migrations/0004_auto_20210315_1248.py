# Generated by Django 3.1.6 on 2021-03-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210311_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role_name',
            field=models.CharField(choices=[('manager', 'MANAGER'), ('normal user', 'NORMAL USER')], default='normal user', max_length=100),
        ),
    ]
