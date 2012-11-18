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
    url(r'^services/locations/get$', 'reclaimphilly_web.rest_services.get_locations'),
)
