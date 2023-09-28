from email.policy import default
from django.forms import ModelForm, Form, CharField, BooleanField
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


class ProfileChangeForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]

class VerifyForm(Form):
    code = CharField(max_length=8, required=True, help_text='Enter code')

class ReSendCode(Form):
    pass


class CustomSignupForm(SignupForm):
    agree_terms = BooleanField(required=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
