"""comp3335 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^search/', include('comp3335.search.urls')),
    url(r'^update/', include('comp3335.update.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('comp3335.dashboard.urls')),

    url(r'^$', include('comp3335.welcome.urls')),
    url(r'^account/', include('comp3335.account.urls')),
    url(r'^welcome/', include('comp3335.welcome.urls')),
]
