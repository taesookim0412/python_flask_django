from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'books/(?P<bookid>\d+)$', views.viewbook),
    url(r'addbook$', views.addbook),
    url(r'authors$', views.authors),
    url(r'authors/(?P<authorid>\d+)$', views.viewauthor),
    url(r'addauthor$', views.addauthor),
]