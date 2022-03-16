# Generated by Django 3.2.9 on 2022-03-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_auto_20220316_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='product_gladns_site_a',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_gladns_site_a_set', to='order.Gladns'),
        ),
        migrations.AlterField(
            model_name='component',
            name='product_gladns_site_b',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_gladns_site_b_set', to='order.Gladns'),
        ),
        migrations.AlterField(
            model_name='component',
            name='product_gladns_site_c',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_gladns_site_c_set', to='order.Gladns'),
        ),
        migrations.AlterField(
            model_name='component',
            name='product_gladns_site_d',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_gladns_site_d_set', to='order.Gladns'),
        ),
        migrations.AlterField(
            model_name='component',
            name='produkt_terminal',
            field=models.ManyToManyField(blank=True, null=True, related_name='terminals_set', to='order.Terminals'),
        ),
    ]
