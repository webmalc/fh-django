from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse
from .models import Payment
from .forms import FinancesForm
from taggit.models import Tag


class PaymentCreate(SuccessMessageMixin, CreateView):
    """
    Payment create view
    """
    model = Payment
    form = FinancesForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was created successfully"


class PaymentUpdate(SuccessMessageMixin, UpdateView):
    """
    Payment update view
    """
    model = Payment
    form = FinancesForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was updated successfully"


class PaymentList(ListView):
    """
    Payments list view
    """
    model = Payment


class PaymentDelete(DeleteView):
    """
    Payment delete view
    """
    model = Payment
    success_url = reverse_lazy('finances:payments_list')
    template_name = "partials/confirm_delete.html"
    success_message = "Payment was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PaymentDelete, self).delete(request, *args, **kwargs)


def tags(request, query=None):
    """
    JSON tags list
    :param request:
    :param query:
    :return: JsonResponse
    """
    items = Tag.objects
    if query:
        items = items.filter(name__contains=query.strip())
    data = [tag.name for tag in items.order_by('name').all()]
    return JsonResponse(data, safe=False)



