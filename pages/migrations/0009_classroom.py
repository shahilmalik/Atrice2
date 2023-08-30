# Generated by Django 4.2.4 on 2023-08-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_uploadedimage_lastspotted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('strength', models.IntegerField(blank=True, default=None, null=True)),
                ('latecomers', models.IntegerField(blank=True, default=None, null=True)),
                ('absents', models.IntegerField(blank=True, default=None, null=True)),
                ('presents', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]