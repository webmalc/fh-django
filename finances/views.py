from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from .models import Payment
from .forms import FinancesForm
from taggit.models import Tag


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


class PaymentList(ListView):
    model = Payment


def tags(request, query=None):
    items = Tag.objects
    if query:
        items = items.filter(name__contains=query.strip())
    data = [tag.name for tag in items.order_by('name').all()]
    return JsonResponse(data, safe=False)



