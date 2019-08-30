# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#from rest_framework import generics
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from .models import Geolocation
from .models import Coupons
import math


# this is a helper function that calculates if a user location falls within the bounds of a geofence
# parameters: 
# location - object that includes latitude and longitude of request
# fence - object that includes particular geofence information
# output: tuple, with first postion as a boolean indicating if hit, and second position denoting distance
def fence_check(location, fence):
    
    # distance formula
    lat_diff = fence[0] - location[0]
    
    long_diff = fence[1] - location[1]
    
    dist = math.sqrt(lat_diff * lat_diff + long_diff * long_diff)
    
    return ((dist < fence[2]), dist) 

# this function is called when the GET reuqest reaches the server
def get_geofences(request):

	try:

		if request.method == "GET":
			
			user_Lat = 0.0
			user_Long = 0.0
			min_Fence_Dist = None
			min_Fence = None
			fence_Info = {}
			coupons = {}

			if request.GET.has_key('latitude'): 
				user_Lat = float(request.GET['latitude'])
			else: 
				return HttpResponseBadRequest('<h1>400 BAD REQUEST</h1><p>INCORRECT REQUEST MADE. PLEASE INCLUDE A LATITUDE ARGUMENT IN YOUR REQUEST</p>')
			
			if request.GET.has_key('longitude'): 
				user_Long = float(request.GET['longitude'])
			else: 
				return HttpResponseBadRequest('<h1>400 BAD REQUEST</h1><p>INCORRECT REQUEST MADE. PLEASE INCLUDE A LONGITUDE ARGUMENT IN YOUR REQUEST</p>')

			# getting the closest geofence that was hit by the user
			for fence in Geolocation.objects.all():
				
			 	hit_Geofence = fence_check((user_Lat, user_Long), [fence.latitude, fence.longitude, fence.radius])
			 	
			 	# we hit the geofence, so check if it is minimum distance to location so far
			 	if hit_Geofence[0]:
			 		if min_Fence_Dist == None or hit_Geofence[1] < min_Fence_Dist:
			 			min_Fence_Dist = hit_Geofence[1]
			 			min_Fence = fence

			# getting all the coupons of the hit geofence
			for coupon in Coupons.objects.filter(fence_id = min_Fence.fence_id):
				coupons[coupon.coupon_id] = coupon.coupon_text

			# building the json data to return 
			fence_Info["latitude"] = min_Fence.latitude
			fence_Info["longitude"] = min_Fence.longitude
			fence_Info["location_name"] = min_Fence.location_name
			fence_Info["location_address"] = min_Fence.location_addr
			fence_Info['coupons'] = coupons

			return JsonResponse(fence_Info)

	except Exception as err:
		print "GOT AN EXPCEPTION ERROR IN get_geofences.\n" + str(err)


