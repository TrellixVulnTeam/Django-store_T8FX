# Generated by Django 2.2.4 on 2019-08-30 10:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20190830_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 1, 10, 5, 49, 371369, tzinfo=utc)),
        ),
    ]