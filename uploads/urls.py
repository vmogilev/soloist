from django.conf.urls import url

from . import views


app_name = 'uploads'
urlpatterns = [
    url(r'^get/(?P<cpa_id>\d+)/(?P<file_name>.*)$', views.download, name='download'),
]
