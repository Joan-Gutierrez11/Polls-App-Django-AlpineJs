from typing import List

from django.db import models

from core.models import SafeDeleteModel

# Create your models here.

class Poll(SafeDeleteModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, upload_to='polls/images/%Y/%m/%d')
    date_created = models.DateTimeField(auto_created=True, auto_now=True)

class Question(models.Model):
    class TypeQuestion(models.TextChoices):
        MULTIPLE_OPTIONS = 'multiple-opt'
        UNIQUE_OPTIONS = 'unique-opt'

    sentence = models.CharField(max_length=250, null=False)
    type_question = models.CharField(max_length=20, choices=TypeQuestion.choices, default=TypeQuestion.UNIQUE_OPTIONS)
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE, null=False)

class Option(models.Model):
    sentence = models.CharField(max_length=250, null=False)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE, null=False)
