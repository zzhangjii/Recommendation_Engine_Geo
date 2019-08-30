from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^app/$', views.get_geofences)
    url(r'^', views.get_geofences)
]