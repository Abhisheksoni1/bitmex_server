from django import forms


class LogDataForm(forms.Form):
    data = forms.CharField(max_length=9632)