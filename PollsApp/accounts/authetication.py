from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class AdminLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('polls:index')

class AdminLogoutView(LogoutView):
    next_page = None

    def get_success_url(self):
        return reverse_lazy('accounts:login')