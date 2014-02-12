from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'teams.views.all_teams'),
    url(r'^myteam/$', 'teams.views.my_team'),
    # url(r'^blog/', include('blog.urls')),

)
