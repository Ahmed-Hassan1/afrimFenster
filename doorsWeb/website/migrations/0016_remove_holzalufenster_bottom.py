# Generated by Django 3.2.25 on 2024-06-26 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_remove_holzalufenster_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holzalufenster',
            name='bottom',
        ),
    ]
