# Generated by Django 4.0.4 on 2022-07-16 22:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_restaurant_personal_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_ordered', models.DateField(verbose_name='Date Ordered')),
                ('price', models.FloatField(blank=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comment', models.TextField(max_length=500)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
    ]
