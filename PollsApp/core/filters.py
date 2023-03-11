from abc import ABC, abstractmethod

from django import forms
from django.http import QueryDict

from django.db import models


class AbstractFilterClass(ABC):
    '''
    
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

class FilterForm(forms.Form):
    filter_class: AbstractFilterClass = None

    @classmethod
    def filter_data_form(cls, query_dict: QueryDict):
        _form = cls(query_dict)
        if _form.is_valid():
            return cls.filter_class.get_filtered_queryset(_form.cleaned_data)
        return cls.filter_class.Meta.model.objects.all()