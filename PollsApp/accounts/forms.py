from django import forms
from django.http import QueryDict

from core.filters import FilterForm

from accounts.filters import UserFilterByUsernameAndEmail
from accounts.models import User

class SearchUserForm(FilterForm):
    filter_class = UserFilterByUsernameAndEmail

    username_email = forms.CharField(
        label='Search',
        max_length=250,
        required=False,
        widget= forms.widgets.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Search by username or email',
            }
        )
    )


class UserCreateForm(forms.ModelForm):
    photo = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={'class': 'form-control'}
        )
    )

    def save(self):
        if self.instance.pk is None:
            new_password = User.objects.make_random_password(length=10)
            self.instance.set_password(new_password)
            self.instance.save()
            return self.instance

        return super(UserCreateForm, self).save()
    
    class Meta:
        model = User
        fields = ('photo', 'username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'first_name': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'last_name': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'email': forms.widgets.EmailInput(attrs= {'class': 'form-control'}),
        }