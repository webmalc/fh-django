import json
from django.views.generic import TemplateView
from finances.models import Payment
from finances.forms import PaymentsFilterForm
import fh.chart


class PaymentsPieChart(TemplateView):
    """
    Payment pie chart view
    """

    template_name = 'analytics/payments_pie_chart.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentsPieChart, self).get_context_data(**kwargs)

        defaults = {'is_incoming': 0}
        form = PaymentsFilterForm(self.request.GET if self.request.GET.get('filter', False) else None, initial=defaults)
        data = form.cleaned_data if form.is_valid() else form.get_initial_data(exclude=('period',))

        context['tags_chart_data'] = fh.chart.get(Payment.objects.tags_by_count(**data))
        context['summary'] = Payment.objects.summary(**data)
        context['form'] = form
        return context
