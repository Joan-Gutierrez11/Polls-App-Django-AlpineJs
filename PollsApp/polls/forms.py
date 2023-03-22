from django import forms

from polls.models import *

class PollForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={'class': 'form-control'}
        )
    )

    questions_objects = forms.JSONField(
        required=False,
        label='',
        widget= forms.widgets.Textarea(attrs={'hidden': 'hidden'})
    )

    def create_poll(self):
        _poll: Poll = super().save()
        questions = self.cleaned_data['questions_objects']

        for question in questions:
            options = question.pop('options')
            _created_question = Question(**question)
            _poll.questions.add(_created_question, bulk=False)

            for opt in options:
                _created_option = Option(**opt)
                _created_question.options.add(_created_option, bulk=False)

        return _poll


    def update_poll(self):
        ...


    def save(self):
        if self.instance.pk is None:
            return self.create_poll()
        
        return self.update_poll()

    class Meta:
        model = Poll
        fields = ('image', 'title', 'description', 'questions_objects')
        widgets = {
            'title': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control'}),
        }


