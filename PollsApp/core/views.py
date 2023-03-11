from django.shortcuts import render

from django.views.generic import ListView
from core.filters import FilterForm

# Create your views here.

class FilterListView(ListView):
    filter_form_class: FilterForm = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.filter_form_class(self.request.GET or None)
        return context
    
    def get_filter_queryset(self):
        return self.filter_form_class.filter_data_form(self.request.GET).order_by('id')

    def get_queryset(self):
        return self.get_filter_queryset()