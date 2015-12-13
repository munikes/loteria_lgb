from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
            url(r'^list/$', login_required(views.IndexView.as_view()), name='index'),
            url(r'^create/$', views.create, name='create_number'),
            url(r'^$', auth_views.login),
            url(r'^logout/$', auth_views.logout),
            ]
