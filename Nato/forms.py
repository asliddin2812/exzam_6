from django import forms
from django.contrib.auth.models import User

from .models import NatoMember

class NatoMemberForm(forms.ModelForm):
    class Meta:
        model = NatoMember
        fields = ['country_name', 'join_date', 'population', 'bio', 'is_active']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email']

