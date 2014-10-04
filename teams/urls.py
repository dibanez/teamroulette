from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url('^$', 'teams.views.main'),

)