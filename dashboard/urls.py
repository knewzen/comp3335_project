from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # ex: /dashboard/5/
    url(r'^(?P<course_id>[a-zA-Z]+[0-9]+)/$', views.coursedetail, name='coursedetail'),

    # ajax: get message
    url(r'^getmessage/$', views.getmessage, name='getmessage'),

]