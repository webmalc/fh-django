from django.test import TestCase
from finances.models import Payment


class PaymentModelTest(TestCase):
    fixtures = ['tests/users.json', 'tests/finances.json', 'tests/taggit.json']

    def test_payment_tags_as_string(self):
        p1 = Payment.objects.get(pk=1)
        p2 = Payment.objects.get(pk=2)
        self.assertEqual(p1.get_tags_as_string(), 'test_one, test_two, test_three')
        self.assertEqual(p2.get_tags_as_string(), '')
