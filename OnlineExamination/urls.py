from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^result/(?P<qn_id>[-\w]+)/$', views.result, name='result'),
    url(r'^timeTable/$', views.time_table, name='time_table'),
]
