from django.conf.urls import url

from . import views


app_name = 'portals'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pa_code>\w+)/clients/$', views.clients, name='clients'),
]

