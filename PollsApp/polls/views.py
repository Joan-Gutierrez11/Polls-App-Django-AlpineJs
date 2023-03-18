from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'base/index.html'

