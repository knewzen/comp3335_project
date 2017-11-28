from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'account/index.html'), name='index'),
    url(r'^register.html', TemplateView.as_view(template_name = 'account/register.html'), name='register'),
    url(r'^register$',views.register),
    url(r'^auth$',views.auth),
    url(r'^dashboard/index.html', TemplateView.as_view(template_name = 'dashboard/index.html'), name='register'),
    url(r'^logout/',views.logout),
]