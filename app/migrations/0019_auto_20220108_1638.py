# Generated by Django 3.0.8 on 2022-01-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_merge_20220107_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_color',
            field=models.CharField(blank=True, choices=[('#5DA7EF', '#5DA7EF'), ('#9ECBFF', '#9ECBFF'), ('#C8D769', '#C8D769'), ('#50B093', '#50B093'), ('#81C7BA', '#81C7BA'), ('#B282CC', '#B282CC'), ('#F85C5D', '#F85C5D'), ('#FFAB41', '#FFAB41'), ('#FFBE6C', '#FFBE6C'), ('#FFD84E', '#FFD84E')], max_length=10, null=True),
        ),
    ]
