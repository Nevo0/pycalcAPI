# Generated by Django 3.2.9 on 2022-03-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20220309_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal',
            name='size',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='terminal',
            name='type',
            field=models.CharField(default='', max_length=200),
        ),
    ]