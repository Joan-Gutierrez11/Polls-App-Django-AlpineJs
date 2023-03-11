from django.urls import path
from django.views.generic import TemplateView

from accounts.views import UserListView

app_name = 'accounts'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('users/', UserListView.as_view(), name='list-users'),
]
