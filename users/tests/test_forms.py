from fh.lib.tests import FormTestCase, ViewTestCase
from users.forms import ValidatingPasswordChangeForm
from users.models import User


class UserFormTest(FormTestCase, ViewTestCase):
    fixtures = ['tests/users.json', 'tests/finances.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_password_form_valid(self):
        """
        Test password form (valid)
        """
        form = ValidatingPasswordChangeForm(user=self.user, data={
            'new_password1': 'qweE58mc4',
            'new_password2': 'qweE58mc4',
            'old_password': 'password'
        })
        self.assertTrue(form.is_valid())

    def test_password_form_invalid(self):
        """
        Test password strength form (invalid)
        """
        form = ValidatingPasswordChangeForm(user=self.user, data={
            'new_password1': '123456',
            'new_password2': '123456',
            'old_password': 'password'
        })
        self.assertFalse(form.is_valid())
