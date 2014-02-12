from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rially.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^submissions/', include('submissions.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^$', 'rially.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
