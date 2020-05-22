from django import forms
from django_select2.forms import Select2MultipleWidget, ModelSelect2MultipleWidget, ModelSelect2Widget

from users.models import CustomUser
from .models import *


########################################################################################
# Date and Time formats
class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


########################################################################################
# Pickup Information Form
class PickupForm(forms.ModelForm):
    pickup_date = forms.DateField(required=True)
    pickup_date.widget = DateInput()
    pickup_time = forms.TimeField(required=True)
    pickup_time.widget = TimeInput()

    class Meta:
        model = Order
        fields = ('pickup_date', 'pickup_time', 'lesson_date', 'lesson_start_time', 'lesson_end_time')
        widgets = {
            'pickup_date': DateInput(),
            'pickup_time': TimeInput(),
            'lesson_date': DateInput(),
            'lesson_start_time': TimeInput(),
            'lesson_end_time': TimeInput()
        }

    def __init__(self, *args, **kwargs):
        super(PickupForm, self).__init__(*args, **kwargs)
        self.fields['lesson_date'].label = "Lesson Date (Optional)"
        self.fields['lesson_start_time'].label = "Lesson Start Time (Optional)"
        self.fields['lesson_end_time'].label = "Lesson End Time (Optional)"


########################################################################################
# Listed & Unlisted add forms
class ListedAddForm(forms.Form):
    quantity = forms.IntegerField(required=True)
    other_notes = forms.CharField(required=False)
    self_filled = forms.BooleanField(required=False)


class UnlistedAddForm(forms.ModelForm):
    class Meta:
        model = OrderContent
        fields = ('item', 'quantity', 'other_notes', 'self_filled')
        widgets = {'order': forms.HiddenInput()}


########################################################################################
# Course forms


class CourseOrderAdd(forms.Form):
    order_number = forms.IntegerField(required=True)
    username = forms.ModelMultipleChoiceField(label='Students', queryset=CustomUser.objects.none(),
                                              widget=Select2MultipleWidget(), required=True)

    class Meta:
        model = CustomUser
        fields = ('username',)
        widgets = {
            'username': Select2MultipleWidget()
        }

    def __init__(self, isUpdate, *args, **kwargs):
        super(CourseOrderAdd, self).__init__(*args, **kwargs)
        self.field_order = ['order_number', 'username']
        self.fields['order_number'].widget.attrs['readonly'] = isUpdate
        self.fields['username'].queryset = CustomUser.objects.all()
