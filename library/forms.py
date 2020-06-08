from django import forms

from library.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class DemoForm(forms.Form):
    checkout_date = forms.DateField(required=True)
    checkout_date.widget = DateInput()

    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'category', 'quantity')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn', 'category', 'quantity')


## PROBLEM
# its kind of ugly looking
# find better way
class NewCheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('checkout_date', 'user_checkout')
        widgets = {
            'checkout_date': DateInput(),
        }


#         TODO:Optimize this, like in cheqroom they searched users ? idk
# and added users if not in databse ?
# class CreateCheckoutForm(forms.ModelForm):
#     checkout_date = forms.DateField(required=True)
#
#     class Meta:
#         model = Checkout
#         fields = ('user_checkout',)

