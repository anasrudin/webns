from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpsb', views.formpsb, name='formpsb'),
    path('sukses', views.sukses, name='sukses'),
    path('list', views.list, name='list'),
]