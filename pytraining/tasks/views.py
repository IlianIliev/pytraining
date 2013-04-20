from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from tasks.models import Task, TaskProposal
from tasks.forms import TaskProposalForm

PAGE_ID = 'tasks'


class TasksListView(ListView):
    context_object_name = 'tasks'
    model = Task

    def get(self, request):
        request.page = PAGE_ID
        return super(TasksListView, self).get(request)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/single_task.html'
    context_object_name = 'task'

    def get(self, request, slug):
        request.page = PAGE_ID
        return super(TaskDetailView, self).get(request, slug)


class ProposeTaskView(CreateView):
    model = TaskProposal
    form_class = TaskProposalForm
    success_url = reverse_lazy('page', args=('thank-you',))
