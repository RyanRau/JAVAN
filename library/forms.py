from datetime import date

from django import forms

from library.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


# TODO: the two weeks thing doesnt work exactly how i want
# TODO: by end of semester max
class DemoForm(forms.Form):
    checkout_date = forms.DateField(required=True, initial=date.today())
    checkout_date.widget = DateInput()
    return_date = forms.DateField(required=True, initial=date.today() + timedelta(days=14))
    return_date.widget = DateInput()

    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'category', 'quantity')


# TODO: Check for existing and errors. this is mad janky. probably other stuff to check for
class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'category', 'quantity')

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')

        if isbn != 'N/A':
            try:
                match = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                return isbn

            raise forms.ValidationError('A book with this isbn already exists')
        else:
            return isbn


class NewCheckoutForm(forms.ModelForm):
    checkout_date = forms.DateField(required=True, initial=date.today())
    return_date = forms.DateField(required=True, initial=date.today() + timedelta(days=14))

    class Meta:
        model = Checkout
        fields = ('checkout_date', 'return_date', 'user_checkout')
        widgets = {
            'checkout_date': DateInput(),
            'return_date': DateInput(),
        }


class EditCheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('checkout_date', 'return_date')
        widgets = {
            'checkout_date': DateInput(),
            'return_date': DateInput(),
        }
