from django import forms
from django.forms import fields
from . import models


class todoForm(forms.ModelForm):
    class Meta:
        model = models.todoModel
        fields = (
            "todo",
            "start_date",
            "end_date",
        )