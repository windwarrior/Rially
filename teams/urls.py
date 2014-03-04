from django.conf.urls import patterns, include, url
from teams.views import TemporaryUserCreateView, TeamView, TeamDetail

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TeamView.as_view(), name='all_teams_view'),
    url(r'^(?P<pk>\d+)/$', TeamDetail.as_view(), name='all_teams_view'),
    url(r'^myteam/$', 'teams.views.my_team'),
    url(r'^myteam/delete/(?P<teamId>\d+)/(?P<userId>\d+)/$', 'teams.views.delete'),
    url(r'^myteam/add/', TemporaryUserCreateView.as_view(), name='team_add_member'),
    # url(r'^blog/', include('blog.urls')),
    url(r'new_teammember/(?P<slug>[\w-]+)/$', 'teams.views.team_confirm', name='team_confirm')
)
