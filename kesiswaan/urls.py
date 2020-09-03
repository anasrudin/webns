from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'kesiswaan'
urlpatterns = [
    path('', views.index, name='indexKesiswaan'),
]