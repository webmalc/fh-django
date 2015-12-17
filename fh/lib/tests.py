from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTestCase(TestCase):

    def _test_unauthorized_view(self, route_name, params={}):
        url = reverse(route_name, kwargs=params)
        redirect = reverse('login') + '?next=' + url
        response = self.client.get(url)
        self.assertRedirects(response, redirect, 302)

    def _login_superuser(self):
        login = self.client.login(username='admin', password='password')
        self.assertEqual(login, True)


class FormTestCase(TestCase):
    pass
