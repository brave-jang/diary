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


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "username",
            "age",
            "first_name",
        )
    password1 = forms.CharField()
    password = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            self.add_error("username", forms.ValidationError("해당 아이디는 이미 존재합니다."))
        except models.User.DoesNotExist:
            return username
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            self.add_error("password", forms.ValidationError("패스워드가 다릅니다."))
        else:
            return password

    def save(self):
        user = super().save(commit=True)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()