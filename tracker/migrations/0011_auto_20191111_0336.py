# Generated by Django 2.2.7 on 2019-11-11 03:36

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20191109_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='observers',
        ),
        migrations.AddField(
            model_name='habit',
            name='observers',
            field=models.ManyToManyField(blank=True, related_name='observers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='habit',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 2, 3, 36, 51, 447856, tzinfo=utc)),
        ),
    ]
