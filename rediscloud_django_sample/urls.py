from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'rediscloud_django_sample.views.home', name='home'),
    url(r'^command$', 'rediscloud_django_sample.views.command', name='command'),
)

urlpatterns += staticfiles_urlpatterns()
