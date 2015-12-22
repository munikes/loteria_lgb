from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
            #url(r'^list/$', login_required(views.LotteryUserList.as_view()), name='lotteryuser-list'),
            url(r'^$', views.LotteryUserList.as_view(), name='lotteryuser-list'),
            url(r'^create/$', login_required(views.LotteryUserCreate.as_view()), name='lotteryuser-create'),
            url(r'^update/(?P<pk>\d+)$', login_required(views.LotteryUserUpdate.as_view()), name='lotteryuser-update'),
            url(r'^delete/(?P<pk>\d+)$', login_required(views.LotteryUserDelete.as_view()), name='lotteryuser-delete'),
            url(r'^logout/$', auth_views.logout, name="logout"),
            #url(r'^$', auth_views.login, name="login"),
            ]
