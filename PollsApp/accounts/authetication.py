from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.urls import reverse_lazy

from accounts.forms import LoginForm

# 
# Custom Login Required Mixin 
# 

class AdminLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('accounts:login')

# 
# Views
# 

class AdminLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('polls:index')

    def form_invalid(self, form):
        messages.error(self.request, 'Login error, incorrect username or password')
        return super().form_invalid(form)

class AdminLogoutView(LogoutView):
    next_page = None

    def get_success_url(self):
        return reverse_lazy('accounts:login')