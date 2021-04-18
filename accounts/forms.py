from django import forms
from . import models

class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드가 틀립니다."))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("해당 아이디가 존재하지 않습니다."))