from django.urls import path
from django.views.generic import TemplateView

from accounts.views import *
from accounts.api_views import UserPrivateAPIView
import accounts.authetication as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.AdminLoginView.as_view(), name='login'),
    path('logout/', auth_views.AdminLogoutView.as_view(), name='logout'),
  
    path('users/', UserListView.as_view(), name='list-users'),
    path('users/add', CreateAdminUserView.as_view(), name='add-users'),
    path('users/update/<int:pk>', UpdateAdminUserView.as_view(), name='update-users'),
    path('users/delete/<int:pk>', DeleteAdminUserView.as_view(), name='delete-users'),
    path('users/safe-delete/<int:pk>', DisableUserAdminView.as_view(), name='safe-delete-users'),

    path('users/api/users-list/', UserPrivateAPIView.as_view(), name='api-private-list-users')
    
]
