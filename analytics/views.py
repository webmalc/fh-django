from django.views.generic import TemplateView
from finances.models import Payment


class PaymentsPieChart(TemplateView):
    """
    Payment pie chart view
    """

    template_name = 'analytics/payments_pie_chart.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentsPieChart, self).get_context_data(**kwargs)

        return context
