# Generated by Django 3.0.8 on 2022-01-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220105_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(default='url', max_length=50),
        ),
    ]
