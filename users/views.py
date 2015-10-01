from django.views.generic import TemplateView


class Profile(TemplateView):
    """
    Profile view
    """

    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)

        return context
