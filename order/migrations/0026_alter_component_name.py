# Generated by Django 3.2.9 on 2022-03-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_terminals_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.TextField(default=''),
        ),
    ]