from django.views.generic import TemplateView
from finances.models import Payment
from finances.forms import PaymentsFilterForm
import fh.chart


class PaymentsChart(TemplateView):
    """
    Payment pie chart view
    """

    template_name = 'analytics/payments_chart.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentsChart, self).get_context_data(**kwargs)

        defaults = {'is_incoming': 0}
        form = PaymentsFilterForm(self.request.GET if self.request.GET.get('filter', False) else None, initial=defaults)
        data = form.cleaned_data if form.is_valid() else form.get_initial_data(exclude=('period',))
        tags = Payment.objects.filtered_tags(**data)
        context['tags_chart_data'] = fh.chart.get(Payment.objects.tags_by_count(filtered_tags=tags, **data))
        context['payment_tags_chart_data'] = fh.chart.get(Payment.objects.tags_by_amount(filtered_tags=tags, **data))
        context['summary'] = Payment.objects.summary(**data)
        context['form'] = form
        return context
