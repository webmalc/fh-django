from django.views.generic import TemplateView


class PaymentsPieChart(TemplateView):
    template_name = 'analytics/payments_pie_chart.html'
