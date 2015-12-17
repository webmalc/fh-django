from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from fh.forms import ModelFormWidgetMixin
from django.core.urlresolvers import reverse_lazy
from tasks.models import Task


class TaskFormViewMixin:
    """
    Task form mixin
    """
    model = Task
    fields = ['title']
    widgets = []


class TaskCreate(SuccessMessageMixin, TaskFormViewMixin, ModelFormWidgetMixin, CreateView):
    """
    Task create view
    """
    success_message = "Task was created successfully"
    success_url = reverse_lazy('tasks:payments_list')
    pass


class TaskUpdate(SuccessMessageMixin, TaskFormViewMixin, ModelFormWidgetMixin, UpdateView):
    """
    Task update view
    """
    success_message = "Task was updated successfully"
    pass


class TaskList(ListView):
    """
    Task list view
    """
    pass


class TaskDelete(DeleteView):
    """
    Task delete view
    """
    pass

