"""soloist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^p/', include('soloist.apps.portals.urls')),
    url(r'^c/', include('soloist.apps.clients.urls')),
    url(r'^l/', include('soloist.apps.categories.urls')),
    url(r'^t/', include('soloist.apps.projects.urls')),
    url(r'^s/', include('soloist.apps.search.urls')),
    url(r'^files/', include('soloist.apps.uploads.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', view=auth_views.login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', view=auth_views.logout, kwargs={'next_page': '/p'}, name='logout'),
]
