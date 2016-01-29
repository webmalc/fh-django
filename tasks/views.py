from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from fh.forms import ModelFormWidgetMixin
from django.core.urlresolvers import reverse_lazy
from django import forms
from tasks.models import Task


class TaskFormViewMixin:
    """
    Task form mixin
    """
    model = Task
    fields = ['title', 'date', 'remind', 'tags', 'priority', 'assigned_to', 'comment', 'is_completed']
    widgets = {
        'date': forms.DateTimeInput(attrs={'placeholder': '2015-11-24 14:59:19', 'class': 'datetimepicker'}),
        'comment': forms.Textarea(attrs={'rows': 5}),
        'priority': forms.Select(attrs={'class': 'not-select2'})
    }


class TaskCreate(SuccessMessageMixin, TaskFormViewMixin, ModelFormWidgetMixin, CreateView):
    """
    Task create view
    """
    success_message = "Task was created successfully"
    success_url = reverse_lazy('tasks:tasks_list')


class TaskUpdate(SuccessMessageMixin, TaskFormViewMixin, ModelFormWidgetMixin, UpdateView):
    """
    Task update view
    """
    success_message = "Task was updated successfully"
    success_url = reverse_lazy('tasks:tasks_list')


class TaskList(ListView):
    """
    Task list view
    """
    pass


class TaskDelete(DeleteView):
    """
    Task delete view
    """
    model = Task
    success_url = reverse_lazy('tasks:tasks_list')
    template_name = "partials/confirm_delete.html"
    success_message = "Task was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDelete, self).delete(request, *args, **kwargs)
