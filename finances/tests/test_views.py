from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class PaymentViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tests/finances.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_payment_list_unauthorized_view(self):
        """
        Test payments list unauthorized view
        """
        self._test_unauthorized_view('finances:payments_list')

    def test_payment_list_view(self):
        """
        Test payments list view
        """
        self._login_superuser()
        url = reverse('finances:payments_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Payments list')
        self.assertContains(response, '2,512.34')
        self.assertContains(response, '14,487.66')

    def test_payment_list_filtered_view(self):
        """
        Test payments list (filtered) view
        """
        self._login_superuser()
        url = reverse('finances:payments_list')
        response = self.client.get(url, {
            'begin': '2015-05-01',
            'end': '2015-08-01',
            'is_incoming': 1,
            'filter': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Payments list')
        self.assertContains(response, '20,000.00')
        self.assertNotContains(response, '2,512.34')

    def test_payment_add_unauthorized_view(self):
        """
        Test payments add unauthorized view
        """
        self._test_unauthorized_view('finances:payment_add')

    def test_payment_edit_unauthorized_view(self):
        """
        Test payments edit unauthorized view
        """
        self._test_unauthorized_view('finances:payment_update', {'pk': 1})

    def test_payment_edit_view(self):
        """
        Test payments edit view
        """
        self._login_superuser()
        url = reverse('finances:payment_update', args=(3,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Change payment #3')
        self.assertContains(response, 'test_two')

    def test_payment_delete_unauthorized_view(self):
        """
        Test payments edit unauthorized view
        """
        self._test_unauthorized_view('finances:payment_delete', {'pk': 1})

    def test_payment_delete_unauthorized_view(self):
        """
        Test payments delete view
        """
        self._login_superuser()
        url = reverse('finances:payment_delete', args=(2,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete payment #2')
