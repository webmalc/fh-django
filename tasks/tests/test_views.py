from fh.lib.tests import ViewTestCase
from django.core.urlresolvers import reverse
from users.models import User


class TaskViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tests/tasks.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_tasks_add_unauthorized_view(self):
        """
        Test payments add unauthorized view
        """
        self._test_unauthorized_view('tasks:task_add')
