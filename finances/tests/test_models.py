from django.test import TestCase
from django.core.urlresolvers import reverse
from users.models import User


class PaymentTest(TestCase):
    fixtures = ['fh.json']

    def setUp(self):
        self.username = 'test'
        self.password = 'password'
        self.user = User.objects.create_superuser(self.username, 'test@example.com', self.password)

    def test_payment_list_unauthorized_view(self):
        url = reverse('finances:payments_list')
        redirect = reverse('login') + '?next=' + url
        response = self.client.get(url)
        self.assertRedirects(response, redirect, 302)

    def test_payment_list_view(self):
        url = reverse('finances:payments_list')
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payments list")
