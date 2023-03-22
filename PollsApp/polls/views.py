from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView

from polls.forms import PollForm

from accounts.authetication import AdminLoginRequiredMixin


# Create your views here.
class IndexView(AdminLoginRequiredMixin, TemplateView):
    template_name = 'base/index.html'

class ListPollsView(AdminLoginRequiredMixin, TemplateView):
    template_name = 'polls/polls/list_polls.html'

class CreatePollView(AdminLoginRequiredMixin, CreateView):
    template_name = 'polls/polls/add_polls.html'
    form_class = PollForm
    success_url = reverse_lazy('polls:add-polls')