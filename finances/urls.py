try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from .views import PaymentCreate, PaymentUpdate

urlpatterns = [
    url(r'payment/add/$', PaymentCreate.as_view(), name='payment_add'),
    url(r'payment/(?P<pk>[0-9]+)/$', PaymentUpdate.as_view(), name='payment_update'),
]
