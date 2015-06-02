from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tilesets/', include('tilebundler.urls', namespace="tilesets")),
    url(r'^admin/', include(admin.site.urls)),
)