from rest_framework import serializers
from polls.models import *


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'sentence')

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'type_question', 'sentence', 'options')

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'