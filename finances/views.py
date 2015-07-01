from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Payment

class PaymentCreate(SuccessMessageMixin, CreateView):
    model = Payment
    fields = ['amount', 'is_incoming']
    success_message = "Payment was created successfully"


class PaymentUpdate(SuccessMessageMixin, UpdateView):
    model = Payment
    fields = ['amount', 'is_incoming']
    success_message = "Payment was updated successfully"



