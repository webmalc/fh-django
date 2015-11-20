from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class AnalyticsViewTest(ViewTestCase):
    fixtures = ['tests/users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_payment_chart_unauthorized_view(self):
        """
        Test payments list unauthorized view
        """
        self._test_unauthorized_view('analytics:payment_chart')
