from django.test import TestCase
from tasks.models import Task


class TaskModelTest(TestCase):
    fixtures = ['tests/users.json', 'tests/tasks.json', 'tests/taggit.json']

    def test_task_tags_as_string(self):
        """
        Test get_tags_to_as_string method
        """
        t1 = Task.objects.get(pk=1)
        t2 = Task.objects.get(pk=2)
        self.assertEqual(t1.get_tags_as_string(), 'test_two, test_one')
        self.assertEqual(t2.get_tags_as_string(), '')

    def test_task_assigned_to_as_string(self):
        """
        Test get_assigned_to_as_string method
        """
        t1 = Task.objects.get(pk=1)
        t2 = Task.objects.get(pk=2)
        self.assertEqual(t1.get_assigned_to_as_string(), 'All')
        self.assertEqual(t2.get_assigned_to_as_string(), 'LastName FirstName, LastName 2 FirstName 2')
