from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages

from core.filters import FilterListView

from accounts.forms import FilterUserForm, UserCreateForm
from accounts.models import User

class UserListView(FilterListView):
    '''
    View that show the users registered in page
    '''
    template_name = 'accounts/users/list_users.html'
    context_object_name = 'users'
    paginate_by = 10
    filter_form_class = FilterUserForm

class CreateAdminUserView(CreateView):
    template_name = 'accounts/users/add_users.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:add-users')

    def form_valid(self, form):
        messages.success(self.request, 'User created successfully')
        return super(CreateAdminUserView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error when create user. Please check the following fields:')
        return super(CreateAdminUserView, self).form_invalid(form)

class UpdateAdminUserView(UpdateView):
    template_name = 'accounts/users/update_users.html'
    model = User
    form_class = UserCreateForm

    def _handle_photo_on_error(self, form):
        self.object.photo = form.initial.get("photo", None)

    def get_success_url(self):
        return reverse_lazy('accounts:update-users', kwargs={ 'pk': self.kwargs['pk'] })

    def form_valid(self, form):
        messages.success(self.request, 'User updated successfully')
        return super(UpdateAdminUserView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error when update user. Please check the following fields:')
        self._handle_photo_on_error(form)
        return super(UpdateAdminUserView, self).form_invalid(form)

class DeleteAdminUserView(DeleteView):
    template_name = "accounts/users/delete_users.html"
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('accounts:list-users')

    def form_valid(self, form):
        messages.success(self.request, f'User ({self.get_object()}) deleted sucessfully')
        return super().form_valid(form)

class DisableUserAdminView(DeleteView):
    template_name = "accounts/users/disable_users.html"
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('accounts:list-users')

    def form_valid(self, form):
        _user: User = self.object
        _user.safe_delete()
        messages.success(self.request, f'User ({self.get_object()}) has been disabled')
        return HttpResponseRedirect(self.get_success_url())
        