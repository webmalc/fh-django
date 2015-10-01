from django.views.generic import TemplateView
from finances.models import Payment
from finances.forms import PaymentsFilterForm
import fh.chart


class PaymentsChart(TemplateView):
    """
    Charts view
    """

    template_name = 'analytics/payments_chart.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentsChart, self).get_context_data(**kwargs)

        form = PaymentsFilterForm(self.request.GET if self.request.GET.get('filter', False) else None,
                                  initial={'is_incoming': 0})
        initial = form.get_initial_data(exclude=('period',))
        initial.update({'is_incoming': False})
        data = form.cleaned_data if form.is_valid() else initial
        tags = Payment.objects.filtered_tags(**data)

        context['tags_chart_data'] = fh.chart.get(Payment.objects.tags_by_count(filtered_tags=tags, **data))
        context['payment_tags_chart_data'] = fh.chart.get(Payment.objects.tags_by_amount(filtered_tags=tags, **data))
        context['payment_days_chart_data'] = fh.chart.get(Payment.objects.payments_by_days(**data), y='amount')
        context['payment_months_chart_data'] = fh.chart.get(Payment.objects.payments_by_months(**data), y='amount')
        context['summary'] = Payment.objects.summary(**data)
        context['form'] = form
        context['filter'] = data

        return context
