from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from polls.models import *
from polls.serializers import PollSerializer

class PollPrivateAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()