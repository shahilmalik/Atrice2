# Generated by Django 4.2.4 on 2023-08-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_uploadedimage_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='lastspotted',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]