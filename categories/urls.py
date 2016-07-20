from django.conf.urls import url

from . import views


app_name = 'categories'
urlpatterns = [
    url(r'^(?P<pa_code>\w+)/(?P<pca_code>\w+)/(?P<cca_id>\d+)$', views.projects, name='projects'),
]
