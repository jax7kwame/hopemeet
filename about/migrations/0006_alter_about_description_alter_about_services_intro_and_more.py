# Generated by Django 5.0.4 on 2024-05-09 13:34

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_teammember_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='services_intro',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
