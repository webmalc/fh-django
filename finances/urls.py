from django.contrib.auth.decorators import permission_required
from django.conf.urls import url

import finances.views as views

urlpatterns = [
    url(r'payment/add/$', permission_required('finances.add_payment')(views.PaymentCreate.as_view()),
        name='payment_add'),
    url(r'payment/$', permission_required('finances.add_payment')(views.PaymentList.as_view()), name='payments_list'),
    url(r'payment/(?P<pk>[0-9]+)/$', permission_required('finances.change_payment')(views.PaymentUpdate.as_view()),
        name='payment_update'),
    url(r'payment/(?P<pk>[0-9]+)/delete$',
        permission_required('finances.delete_payment')(views.PaymentDelete.as_view()), name='payment_delete'),
]
