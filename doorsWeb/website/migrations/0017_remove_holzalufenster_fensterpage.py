# Generated by Django 3.2.25 on 2024-06-26 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_remove_holzalufenster_bottom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holzalufenster',
            name='fensterpage',
        ),
    ]
