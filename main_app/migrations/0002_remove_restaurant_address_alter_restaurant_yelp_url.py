# Generated by Django 4.0.4 on 2022-07-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='yelp_url',
            field=models.CharField(max_length=100),
        ),
    ]
