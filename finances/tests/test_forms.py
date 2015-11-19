from fh.lib.tests import FormTestCase
from finances.forms import PaymentsFilterForm
from datetime import date, timedelta


class PaymentFormTest(FormTestCase):
    fixtures = []

    def test_payments_filter_form_valid(self):
        """
        Test payments filter form (valid)
        """
        form = PaymentsFilterForm({
            'begin': date.today(),
            'end': date.today() + timedelta(weeks=3),
        })
        self.assertTrue(form.is_valid())

    def test_payments_filter_form_invalid(self):
        """
        Test payments filter form (invalid)
        """
        form = PaymentsFilterForm({})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors, {
            'begin': ['This field is required.'],
            'end': ['This field is required.']
        })
