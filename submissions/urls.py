from django.conf.urls import patterns, include, url

from submissions.views import SubmissionCreate, SubmissionUpdate, SubmissionDelete, SubmissionTeamView, \
    AssignmentView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'submissions.views.index'),
    url(r'new/$', SubmissionCreate.as_view(), name='submission_new'),
    url(r'update/(?P<pk>\d+)/$', SubmissionUpdate.as_view(), name='submission_edit'),
    url(r'delete/(?P<pk>\d+)/$', SubmissionDelete.as_view(), name='submission_delete'),
    url(r'mysubmission/', SubmissionTeamView.as_view(), name='submission_list'),
    url(r'assignments/', AssignmentView.as_view(), name='assignment_list')
)
