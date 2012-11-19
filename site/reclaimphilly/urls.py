from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reclaimphilly.views.home', name='home'),
    # url(r'^reclaimphilly/', include('reclaimphilly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^services/locations/latitude/(?P<latitude>[+-]?\d{1,2}(\.\d{1,13})?)/longitude/(?P<longitude>[+-]?\d{1,3}(\.\d{1,13})?)/radius/(?P<radius>[+-]?\d{1,5}(\.\d{1,13})?)', 'reclaimphilly_web.rest_services.get_locations'),
    url(r'^services/locations/id/(?P<id>\d+)', 'reclaimphilly_web.rest_services.get_location_detail'),
)
