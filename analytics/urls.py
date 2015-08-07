from django.contrib.auth.decorators import permission_required
from django.conf.urls import url

import analytics.views as views

urlpatterns = [
    url(r'charts/payments/pie$', permission_required('finances.add_payment')(views.PaymentsChart.as_view()),
        name='payment_pie_chart'),
]
