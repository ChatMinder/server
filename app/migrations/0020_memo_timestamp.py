# Generated by Django 3.0.8 on 2022-01-08 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20220108_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='timestamp',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
