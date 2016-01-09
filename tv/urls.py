from django.conf.urls import url

import tv.views as views

urlpatterns = [
    url(r'channel/$', views.ChannelList.as_view(), name='channels_list'),
    url(r'channel/(?P<pk>[0-9]+)/$', views.ChannelShow.as_view(), name='channel_show'),
]
