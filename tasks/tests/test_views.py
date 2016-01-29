from fh.lib.tests import ViewTestCase
from users.models import User


class TaskViewTest(ViewTestCase):
    fixtures = ['tests/users.json', 'tests/tasks.json', 'tests/taggit.json', 'fh.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_tasks_list_unauthorized_view(self):
        """
        Test tasks list unauthorized view
        """
        self._test_unauthorized_view('tasks:tasks_list')

    def test_task_add_unauthorized_view(self):
        """
        Test tasks add unauthorized view
        """
        self._test_unauthorized_view('tasks:task_add')

    def test_task_edit_unauthorized_view(self):
        """
        Test tasks edit unauthorized view
        """
        self._test_unauthorized_view('tasks:task_update', {'pk': 1})
        
    def test_task_delete_unauthorized_view(self):
        """
        Test tasks edit unauthorized view
        """
        self._test_unauthorized_view('tasks:task_delete', {'pk': 1})    