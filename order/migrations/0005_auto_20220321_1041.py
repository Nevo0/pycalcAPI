# Generated by Django 3.2.9 on 2022-03-21 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220321_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaser',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='weight',
        ),
    ]
