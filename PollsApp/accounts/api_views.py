from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import UserSerializer
from accounts.models import User

class UserPrivateAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
