# Generated by Django 5.0.4 on 2024-05-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='uploads/group_logos')),
                ('fb_link', models.CharField(blank=True, max_length=255, verbose_name='facebook link')),
                ('ig_link', models.CharField(blank=True, max_length=255, verbose_name='instagram link')),
                ('tiktok_link', models.CharField(blank=True, max_length=255)),
                ('x_link', models.CharField(blank=True, max_length=255, verbose_name='x link')),
            ],
        ),
    ]
