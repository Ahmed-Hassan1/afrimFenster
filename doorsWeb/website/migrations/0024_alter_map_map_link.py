# Generated by Django 3.2.25 on 2024-06-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='map_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
