from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'date_joined')