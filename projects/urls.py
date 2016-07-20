from django.conf.urls import url

from . import views


app_name = 'projects'
urlpatterns = [
    url(r'^(?P<pa_code>\w+)/(?P<pca_code>\w+)-(?P<cpa_id>\d+)$', views.worklogs, name='worklogs'),
]
