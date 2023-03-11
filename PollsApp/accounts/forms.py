from django import forms
from django.http import QueryDict

from core.filters import FilterForm
from accounts.filters import UserFilterByUsernameAndEmail

class SearchUserForm(FilterForm):
    filter_class = UserFilterByUsernameAndEmail

    username_email = forms.CharField(
        label='Search',
        max_length=250,
        required=False,
        widget= forms.widgets.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Search by username or email',
            }
        )
    )
