from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'teamroulette.views.home', name='home'),
    url(r'^teams/', include('teams.urls', namespace='teams')),

    url(r'^api/', include('teams.urls', namespace='teams')),

    url(r'^token/', 'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^admin/', include(admin.site.urls)),
)
