try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

import finances.views as views

urlpatterns = [
    url(r'tags/$', views.tags, name='tags_all'),
    url(r'tags/(?P<query>.+)/$', views.tags, name='tags_query'),
    url(r'payment/add/$', views.PaymentCreate.as_view(), name='payment_add'),
    url(r'payment/$', views.PaymentList.as_view(), name='payments_list'),
    url(r'payment/(?P<pk>[0-9]+)/$', views.PaymentUpdate.as_view(), name='payment_update'),
    url(r'payment/(?P<pk>[0-9]+)/delete$', views.PaymentDelete.as_view(), name='payment_delete'),
]
