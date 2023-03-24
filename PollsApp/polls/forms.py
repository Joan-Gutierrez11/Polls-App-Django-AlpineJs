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

    def clean_questions_objects(self):
        questions = self.cleaned_data["questions_objects"]
        questions = list(filter(lambda q: q['sentence'] != '' and q['type_question'] != '', questions))
        for q in questions:
            q['options'] = list(filter(lambda opt: opt['sentence'] != '', q['options']))
        return questions

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
        _poll: Poll = super().save()
        questions = self.cleaned_data['questions_objects']
        
        questions_updated_ids = []
        options_updated_ids = []

        for q in questions:
            options = q.pop('options')
            _question = Question(**q)
            _question.poll = _poll
            _question.save()
            questions_updated_ids.append(_question.id)

            for option in options:
                _opt = Option(**option)
                _opt.question = _question
                _opt.save()
                options_updated_ids.append(_opt.id)

        Option.objects.filter(question__poll=_poll).exclude(id__in=options_updated_ids).delete()
        _poll.questions.exclude(id__in=questions_updated_ids).delete()

        return _poll

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


