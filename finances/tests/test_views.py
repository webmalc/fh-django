from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class PaymentViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tests/finances.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_payment_list_unauthorized_view(self):
        self._test_unauthorized_view('finances:payments_list')

    def test_payment_list_view(self):
        self._login_superuser()
        url = reverse('finances:payments_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payments list")
        self.assertContains(response, '2,512.34')

    def test_payment_add_unauthorized_view(self):
        self._test_unauthorized_view('finances:payments_add')

    def test_payment_add_view(self):
        pass
