from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'account/index.html'), name='index'),
    url(r'^register.html', TemplateView.as_view(template_name = 'account/register.html'), name='register'),
    url(r'^register/$',views.register , name='register'),
    url(r'^auth/$',views.auth , name='auth'),
]