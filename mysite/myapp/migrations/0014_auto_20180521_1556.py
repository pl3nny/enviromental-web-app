# Generated by Django 2.0.2 on 2018-05-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_posts_city_official'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='city_official',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdata',
            name='location',
            field=models.CharField(default='San Francisco', max_length=255),
        ),
    ]
