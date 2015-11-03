from django.views.generic import TemplateView, UpdateView, RedirectView
from django.contrib.messages.views import SuccessMessageMixin
from finances.models import Payment
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class PasswordChangeRedirectView(RedirectView):
    """
    Password change done redirect
    """
    permanent = False
    url = reverse_lazy('users:profile')

    def get_redirect_url(self, *args, **kwargs):
        messages.success(self.request, 'Password was updated successfully.')

        return super(PasswordChangeRedirectView, self).get_redirect_url(*args, **kwargs)


class Profile(TemplateView):
    """
    Profile view
    """

    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['payments_total'] = Payment.objects.filter(created_by=self.request.user).count()
        context['average_payment'] = round(
            list(Payment.objects.filter(created_by=self.request.user).filter(is_incoming=False).aggregate(
                Avg('amount')).values())[0], 2)

        return context


class UserUpdate(SuccessMessageMixin, UpdateView):
    """
    User update view
    """
    model = User
    fields = ['last_name', 'first_name', 'email']
    success_url = reverse_lazy('users:profile')
    success_message = "Profile was updated successfully"
    template_name = 'users/profile_edit.html'

    def get_object(self):
        return self.request.user
