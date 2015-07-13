from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tournaments/
    url(r'^$', views.index, name='index'),
    # ex: /tournaments/5/
    url(r'^(?P<tournament_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /tournaments/5/results/
    url(r'^(?P<tournament_id>[0-9]+)/results/$', views.results, name='results'),
]
