# Generated by Django 3.2.9 on 2022-03-21 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220321_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='gladns',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='terminals',
            name='brand',
        ),
    ]