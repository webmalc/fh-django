from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class TvViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tv.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_channels_unauthorized_view(self):
        """
        Test channels list unauthorized view
        """
        self._test_unauthorized_view('tv:channels_list')

    def test_payment_list_view(self):
        """
        Test channels list view
        """
        self._login_superuser()
        url = reverse('tv:channels_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TV')
        self.assertContains(response, '<li class="favorite-channel"><a href="/tv/channel/2/">Discovery</a></li>')
        self.assertContains(response, 'Plus TV')

    def test_channel_show_unauthorized_view(self):
        """
        Test channel show unauthorized view
        """
        self._test_unauthorized_view('tv:channel_show', {'pk': 35})

    def test_channel_show_view(self):
        """
        Test channel show view
        """
        self._login_superuser()
        url = reverse('tv:channel_show', args=(35,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Channel "Da Vinci Learning" ')
