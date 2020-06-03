from django import forms

from library.models import Book


class DemoForm(forms.Form):
    checkout_date = forms.DateField(required=True)
    checkout = forms.BooleanField(required=False)


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'category')
