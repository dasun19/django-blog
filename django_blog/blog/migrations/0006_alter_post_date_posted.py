# Generated by Django 5.1.6 on 2025-03-19 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date_posted_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 19, 4, 59, 44, 161296, tzinfo=datetime.timezone.utc)),
        ),
    ]
