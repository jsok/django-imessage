from django.conf.urls import patterns, include, url

urlpatterns = patterns('messages.views',
    url(r'^$', 'index'),
     url(r'^(?P<handle_id>\d+)/$', 'messages'),
)
