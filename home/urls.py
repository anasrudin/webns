from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpsb', views.formpsb, name='formpsb'),
]