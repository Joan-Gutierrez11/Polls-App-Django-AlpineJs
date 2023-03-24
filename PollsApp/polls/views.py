from django.shortcuts import render

from django.core import serializers
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, UpdateView

from polls.forms import PollForm
from polls.models import *
from polls.serializers import QuestionSerializer

from accounts.authetication import AdminLoginRequiredMixin

import json

# Create your views here.
class IndexView(AdminLoginRequiredMixin, TemplateView):
    template_name = 'base/index.html'

class ListPollsView(AdminLoginRequiredMixin, TemplateView):
    template_name = 'polls/polls/list_polls.html'

class CreatePollView(AdminLoginRequiredMixin, CreateView):
    template_name = 'polls/polls/add_polls.html'
    form_class = PollForm
    success_url = reverse_lazy('polls:add-polls')

    def form_valid(self, form):
        messages.success(self.request, 'Poll created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error when create poll. Please check the following fields:')
        return super().form_invalid(form)

class UpdatePollView(UpdateView):
    template_name = 'polls/polls/update_polls.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse_lazy('polls:update-polls', kwargs={ 'pk': self.kwargs['pk'] })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _questions = QuestionSerializer(self.get_object().questions.all(), many=True)
        context["questions_serialized"] = _questions.data
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Poll updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error when update poll. Please check the following fields:')
        return super().form_invalid(form)