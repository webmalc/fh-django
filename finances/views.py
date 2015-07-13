from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Payment
from .forms import FinancesForm


class PaymentCreate(SuccessMessageMixin, CreateView):
    model = Payment
    form = FinancesForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was created successfully"


class PaymentUpdate(SuccessMessageMixin, UpdateView):
    model = Payment
    form = FinancesForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was updated successfully"



