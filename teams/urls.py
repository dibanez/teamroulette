from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url('^team/$', 'teams.views.team', name='team'),
    url('^player/$', 'teams.views.player', name='player'),
)