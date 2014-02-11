from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'submissions.views.index'),
    url(r'new/$', 'submissions.views.new')
    # url(r'^blog/', include('blog.urls')),

)
