from django.test import TestCase
from users.models import User


class UsersModelTest(TestCase):
    fixtures = ['tests/users.json']

    def test_users_to_string(self):
        user = User.objects.get(pk=1)
        self.assertEqual(str(user), 'LastName FirstName')

