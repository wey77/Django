from . import views
from django.conf.urls import url

urlpatterns = [
    # url('^demo01/$', views.demo_01),
    url(r'^get_loc_arg/(?P<addr>[a-z]+)/(?P<year>\d{4})/$', views.get_loc_arg),
    url(r'^get_quer_arg/$', views.get_quer_arg),
    url(r'^get_req_body/$', views.get_req_body),
    url(r'^get_json_arg/$', views.get_json_arg)
]
