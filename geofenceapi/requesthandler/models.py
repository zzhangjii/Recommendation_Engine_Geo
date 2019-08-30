# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Geolocation(models.Model):

	fence_id = models.PositiveIntegerField()
	location_name = models.CharField(max_length = 50, default = 'NULL')
	location_addr = models.TextField(default = 'NULL') 
	latitude = models.FloatField()
	longitude = models.FloatField()
	radius = models.FloatField()
	fence_id.primary_key = True

class Coupons(models.Model):

	coupon_id = models.PositiveIntegerField()
	coupon_text = models.TextField(default = 'NULL')
	fence_id = models.ForeignKey(Geolocation, on_delete = models.CASCADE)
	coupon_id.primary_key = True



