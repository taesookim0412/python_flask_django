from django.conf.urls import url

urlpatterns = [
    url('shows/new$', views.new),
    url('shows/create$', views.create),
    url('shows/(?P<id>\d+)$', views.show),
    url('shows$', views.index),
    url('shows/(?P<id>\d+)/edit', views.edit),
    url('shows/(?P<id>\d+)/update', views.update),
    url('shows/(?P<id>\d+)/destroy', views.destroy),
]