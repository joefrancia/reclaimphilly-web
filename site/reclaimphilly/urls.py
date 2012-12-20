from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'reclaimphilly_web.views.index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^services/locations', 'reclaimphilly_web.rest_services.get_locations_in_radius'),
    url(r'^services/location/(?P<id>\d+)', 'reclaimphilly_web.rest_services.get_location_by_id'),
    url(r'^services/location', 'reclaimphilly_web.rest_services.add_location'),
)
