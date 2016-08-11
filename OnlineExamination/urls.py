from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^start/(?P<qn_id>[-\w]+)/$', views.start, name='start'),
    url(r'^timeTable/$', views.time_table, name='time_table'),
    url(r'^result/$', views.result, name='result'),
]
