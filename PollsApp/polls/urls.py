from django.urls import path
from polls.views import MainDashboardView, ListPollsView, CreatePollView, UpdatePollView, DeletePollView
from polls.api_views import PollPrivateAPIView

app_name = 'polls'

urlpatterns = [
    path('', MainDashboardView.as_view(), name='index'),

    path('polls/', ListPollsView.as_view(), name='list-polls'),
    path('polls/add', CreatePollView.as_view(), name='add-polls'),
    path('polls/update/<int:pk>', UpdatePollView.as_view(), name='update-polls'),
    path('polls/delete/<int:pk>', DeletePollView.as_view(), name='delete-polls'),
    
    path('polls/api/polls-list/', PollPrivateAPIView.as_view(), name='api-private-list-polls'),
    
]
