from django import forms
from django.http import QueryDict

from core.filters import FilterForm

from accounts.filters import UserFilter
from accounts.models import User

class FilterUserForm(FilterForm):
    OPTIONS = [('', 'Default'),] + User.TypeUsers.choices 
    filter_class = UserFilter

    username = forms.CharField(
        label='Username',
        max_length=50,
        required=False,
        widget= forms.widgets.TextInput(
            attrs={ 'class':'form-control' }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.widgets.EmailInput(
            attrs={ 'class':'form-control' }
        )
    )
    type_user = forms.ChoiceField(
        label='Type of user',
        choices=OPTIONS,
        required=False,
        widget=forms.widgets.Select(
            attrs={ 'class': 'form-select' }
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
        fields = ('photo', 'username', 'first_name', 'last_name', 'email', 'is_active')
        widgets = {
            'username': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'first_name': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'last_name': forms.widgets.TextInput(attrs= {'class': 'form-control'}),
            'email': forms.widgets.EmailInput(attrs= {'class': 'form-control'}),
            'is_active': forms.widgets.CheckboxInput(attrs={'class':'form-check-input ms-0 fs-3'})
        }