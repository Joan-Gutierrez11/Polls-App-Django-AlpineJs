from django.urls import path
from polls.views import IndexView, ListPollsView, CreatePollView, UpdatePollView, DeletePollView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('polls/', ListPollsView.as_view(), name='list-polls'),
    path('polls/add', CreatePollView.as_view(), name='add-polls'),
    path('polls/update/<int:pk>', UpdatePollView.as_view(), name='update-polls'),
    path('polls/delete/<int:pk>', DeletePollView.as_view(), name='delete-polls'),
    
]
