from django.conf.urls import url

from . import views


app_name = 'clients'
urlpatterns = [
    url(r'^(?P<pca_code>\w+)/cat/$', views.categories, name='categories'),
]
