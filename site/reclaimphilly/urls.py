from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reclaimphilly.views.home', name='home'),
    # url(r'^reclaimphilly/', include('reclaimphilly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^$', 'reclaimphilly_web.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^services/get/locations/latitude/(?P<latitude>[+-]?\d{1,2}(\.\d{1,13})?)/longitude/(?P<longitude>[+-]?\d{1,3}(\.\d{1,13})?)/radius/(?P<radius>[+-]?\d{1,5}(\.\d{1,13})?)$', 'reclaimphilly_web.rest_services.get_locations_in_radius'),
    url(r'^services/get/location/id/(?P<id>\d+)', 'reclaimphilly_web.rest_services.get_location_by_id'),
    url(r'^services/put/location/latitude/(?P<latitude>[+-]?\d{1,2}(\.\d{1,13})?)/longitude/(?P<longitude>[+-]?\d{1,3}(\.\d{1,13})?)/type/(?P<type>\w{1,4})(/address/(?P<address>(\w|\.|\s)+))?(/description/(?P<description>(\w|\s|[.?!"_\'-]){1,200}))?$', 'reclaimphilly_web.rest_services.add_location'), # TODO This is a scary regular expression - revise later
    
)
