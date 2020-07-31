from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'classification', 'first_name', 'last_name')

        def is_school_email(self):
            email = self.cleaned_data.get('email')

            email_exists = CustomUser.objects.get(email=email)

            if email_exists:
                raise forms.ValidationError('A user with this email exists.')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'classification')
