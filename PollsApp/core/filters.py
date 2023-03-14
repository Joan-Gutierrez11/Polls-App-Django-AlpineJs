from abc import ABC, abstractmethod

from django import forms
from django.http import QueryDict
from django.views import generic

from django.db import models

# Filter Class

class AbstractFilterClass(ABC):
    '''
    Abtract class for filter class. Is necessary implement 'get_filter' method
    '''
    
    @abstractmethod
    def get_filter(self, query: dict) -> models.Q:
        raise NotImplementedError

    @classmethod
    def get_filtered_queryset(cls, data) -> models.QuerySet:
        data_filter = cls.get_filter(cls, data)
        return cls.Meta.model.objects.filter(data_filter)

    class Meta:
        model: models.Model = None

# Forms

class FilterForm(forms.Form):
    filter_class: AbstractFilterClass = None

    @classmethod
    def filter_data_form(cls, query_dict: QueryDict):
        _form = cls(query_dict)
        if _form.is_valid():
            return cls.filter_class.get_filtered_queryset(_form.cleaned_data)
        return cls.filter_class.Meta.model.objects.all()

# Views

class FilterListView(generic.ListView):
    filter_form_class: FilterForm = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.filter_form_class(self.request.GET or None)
        return context
    
    def get_filter_queryset(self):
        return self.filter_form_class.filter_data_form(self.request.GET).order_by('id')

    def get_queryset(self):
        return self.get_filter_queryset()
