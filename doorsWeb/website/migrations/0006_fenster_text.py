# Generated by Django 3.2.25 on 2024-06-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20240625_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenster',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]