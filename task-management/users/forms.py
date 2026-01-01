from django import forms
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Permission, Group
from tasks.forms import StyleFormMixin

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CustomRegistrationForm(StyleFormMixin, forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []

        if len(password1) < 8:
            errors.append('Password must be at least 8 characters.')

        if not re.search(r'[A-Z]', password1):
            errors.append('Must include an uppercase letter.')

        if not re.search(r'[a-z]', password1):
            errors.append('Must include a lowercase letter.')

        if not re.search(r'[0-9]', password1):
            errors.append('Must include a number.')

        if not re.search(r'[@#$%^&+=]', password1):
            errors.append('Must include a special character.')

        if errors:
            raise forms.ValidationError(errors)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class LoginForm(StyleFormMixin, AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

class AssignRoleForm(StyleFormMixin, forms.Form):
    role = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label='Select a role')

class CreateGroupForm(StyleFormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )
    class Meta:
        model = Group
        fields = ['name', 'permissions']