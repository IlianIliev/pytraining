from django.conf import settings
from django.conf.urls import patterns, include, url

from tasks.views import ProposeTaskView, TasksListView, TaskDetailView


urlpatterns = patterns('',
    url(r'^$', TasksListView.as_view(), name='tasks'),
    url(r'propose-a-task/$', ProposeTaskView.as_view(), name='propose-a-task'),
    url(r'^(?P<slug>[-\w]+)/$', TaskDetailView.as_view(), name='single-task'),
)
