# Generated by Django 3.2.25 on 2024-06-25 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_homepage_ptaghome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fenster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bottom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FensterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FensterPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=250)),
                ('fenster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.fenster')),
            ],
        ),
        migrations.AddField(
            model_name='fenster',
            name='fensterpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.fensterpage'),
        ),
    ]
