# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requesthandler', '0004_auto_20181128_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupons',
            old_name='coupon',
            new_name='couponId',
        ),
        migrations.RenameField(
            model_name='coupons',
            old_name='fence',
            new_name='fenceId',
        ),
        migrations.RenameField(
            model_name='geolocation',
            old_name='fence',
            new_name='fenceId',
        ),
        migrations.AlterField(
            model_name='coupons',
            name='fenceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requesthandler.Geolocation'),
        ),
    ]