from django.urls import path
from polls.views import IndexView, ListPollsView, CreatePollView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('polls/', ListPollsView.as_view(), name='list-polls'),
    path('polls/add', CreatePollView.as_view(), name='add-polls'),
]
