from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class UsersViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tests/finances.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_user_profile_unauthorized_view(self):
        self._test_unauthorized_view('users:profile')

    def test_user_profile_view(self):
        url = reverse('users:profile')
        self._login_superuser()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin`s profile")

    def test_user_profile_edit_unauthorized_view(self):
        self._test_unauthorized_view('users:profile_edit')

    def test_user_profile_edit_view(self):
        url = reverse('users:profile_edit')
        self._login_superuser()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "admin@example.com")
