# Generated by Django 4.2.4 on 2023-08-16 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_uploadedimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='timestamp',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]