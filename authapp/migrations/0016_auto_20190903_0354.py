# Generated by Django 2.2.4 on 2019-09-03 00:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_auto_20190903_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 5, 0, 54, 4, 764990, tzinfo=utc)),
        ),
    ]