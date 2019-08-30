# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Geolocation
from .models import Coupons

# Register your models here.

admin.site.register(Geolocation)
admin.site.register(Coupons)