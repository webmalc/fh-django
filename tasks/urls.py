from django.contrib.auth.decorators import permission_required
from django.conf.urls import url
import tasks.views as views

urlpatterns = [
    url(r'task/add/$', permission_required('tasks.add_task')(views.TaskCreate.as_view()),
        name='task_add'),
    url(r'task/(?P<pk>[0-9]+)/$', permission_required('tasks.change_task')(views.TaskUpdate.as_view()),
        name='task_update'),
    url(r'task/$', permission_required('tasks.add_task')(views.TaskList.as_view()), name='tasks_list'),
    url(r'task/(?P<pk>[0-9]+)/delete$',
        permission_required('tasks.delete_task')(views.TaskDelete.as_view()), name='task_delete'),
]
