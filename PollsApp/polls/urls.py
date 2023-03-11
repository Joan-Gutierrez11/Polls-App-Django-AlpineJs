from django.urls import path
from polls.views import IndexView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
