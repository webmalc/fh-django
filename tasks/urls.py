from django.contrib.auth.decorators import permission_required
from django.conf.urls import url
import tasks.views as views

urlpatterns = [
    url(r'task/add/$', permission_required('tasks.add_task')(views.TaskCreate.as_view()),
        name='task_add'),
]
