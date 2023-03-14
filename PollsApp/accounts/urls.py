from django.urls import path
from django.views.generic import TemplateView

from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    
    path('users/', UserListView.as_view(), name='list-users'),
    path('users/add', CreateAdminUserView.as_view(), name='add-users'),
    path('users/update/<int:pk>', UpdateAdminUserView.as_view(), name='update-users'),
    path('users/delete/<int:pk>', DeleteAdminUserView.as_view(), name='delete-users'),
    path('users/safe-delete/<int:pk>', DisableUserAdminView.as_view(), name='safe-delete-users'),
    
]
