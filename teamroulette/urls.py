from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'teamroulette.views.home', name='home'),
    url(r'^teams/', include('teams.urls', namespace='teams')),

    url(r'^admin/', include(admin.site.urls)),
)
