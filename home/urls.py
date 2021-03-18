from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpsb', views.formpsb, name='formpsb'),
    path('sukses', views.sukses, name='sukses'),
    path('list', views.list, name='list'),
    url(r'^delete-psb/(?P<id>[0-9]+)$', views.deletepsb, name='deletepsb'),
	url(r'^update-psb/(?P<id>[0-9]+)$', views.updatepsb, name='updatepsb'),

]