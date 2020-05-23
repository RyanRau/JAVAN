from django import forms


class DemoForm(forms.Form):
    some_int = forms.IntegerField(required=True)
    some_string = forms.CharField(required=False)
    some_bool = forms.BooleanField(required=False)