# Generated by Django 3.2.9 on 2022-03-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20220323_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaser',
            name='nip',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='vat',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]