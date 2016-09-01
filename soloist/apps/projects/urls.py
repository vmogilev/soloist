from django.conf.urls import url

from . import views


app_name = 'projects'
urlpatterns = [
    url(r'^(?P<pa_code>\w+)/(?P<pca_code>\w+)-(?P<cpa_id>\d+)$', views.worklogs, name='worklogs'),
    url(r'^(?P<pa_code>\w+)/(?P<pca_code>\w+)-(?P<cpa_id>\d+)/(?P<pwa_id>\d+)$', views.detail, name='detail'),
    # url(r'^(?P<pa_code>\w+)/(?P<pca_code>\w+)-(?P<cpa_id>\d+)/(?P<pwa_id>\d+)/edit$', views.edit_worklog, name='edit_worklog'),
    # url(r'^save$', views.save_worklog, name='save_worklog'),
]
