from django.shortcuts import render
from django.views.generic import ListView

from accounts.forms import SearchUserForm

from core.views import FilterListView

class UserListView(FilterListView):
    template_name = 'accounts/users/list_users.html'
    context_object_name = 'users'
    paginate_by = 10
    filter_form_class = SearchUserForm