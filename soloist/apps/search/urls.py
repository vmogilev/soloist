from django.conf.urls import url

from . import views


app_name = 'search'
urlpatterns = [
    url(r'^search$', views.serp, name='serp'),
]