from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse
from .models import Payment
from .forms import PaymentForm, PaymentsFilterForm
from taggit.models import Tag


class PaymentCreate(SuccessMessageMixin, CreateView):
    """
    Payment create view
    """
    model = Payment
    form = PaymentForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was created successfully"
    success_url = reverse_lazy('finances:payments_list')


class PaymentUpdate(SuccessMessageMixin, UpdateView):
    """
    Payment update view
    """
    model = Payment
    form = PaymentForm
    fields = ['tags', 'amount', 'is_incoming']
    success_message = "Payment was updated successfully"


class PaymentList(ListView):
    """
    Payments list view
    """
    THEAD = (
        {'title': 'tags'},
        {'title': 'amount',  'class': 'td-sm text-right',  'sort': 'amount'},
        {'title': 'date', 'class': 'td-md', 'sort': 'date'},
        {'title': 'in', 'class': 'td-xs text-center', 'sort': 'is_incoming'},
        {'title': 'user', 'class': 'td-sm text-center', 'sort': 'created_by'},
    )
    model = Payment
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(PaymentList, self).get_context_data(**kwargs)
        form = PaymentsFilterForm(self.request.GET if self.request.GET.get('filter', False) else None)
        data = form.cleaned_data if form.is_valid() else form.get_initial_data(exclude=('period',))
        context['summary'] = Payment.objects.summary(**data)
        context['thead'] = self.THEAD
        context['form'] = form

        return context

    def get_queryset(self):
        form = PaymentsFilterForm(self.request.GET if self.request.GET.get('filter', False) else None)
        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order')
        data = form.cleaned_data if form.is_valid() else form.get_initial_data(exclude=('period',))
        data.pop("period", None)

        return Payment.objects.filtered(sort=sort, order=order, **data)


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
