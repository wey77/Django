from django.conf.urls import url

# from second.views import outer, Class_View
from . import views
from . import test_day02

urlpatterns = [
    url(r'^test_resp/$', views.test_resp),
    url(r'^test_resp1/$', views.test_resp1),
    url(r'^test_jsonresp/$', views.test_jsonresp, name='test_jsonresp'),
    url(r'^test_redirect/$', views.test_redirect),
    url(r'^test_cookie1/$', views.test_cookie1),
    url(r'^test_session1/$', views.test_session1),
    url(r'^test_session2/$', views.test_session2),
    url(r'^get_cookie/$', views.get_cookie),
    url(r'^Class_View/$', views.Class_View.as_view()),
    url(r'^render_templates/$', views.render_templates),
    url(r'^test/$', test_day02.BookView.as_view())

]