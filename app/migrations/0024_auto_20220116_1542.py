# Generated by Django 3.0.8 on 2022-01-16 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20220111_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memo_tag', to='app.Tag'),
        ),
    ]