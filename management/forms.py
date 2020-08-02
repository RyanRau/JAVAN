from django import forms

from materials.models import Order


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status', 'master_teacher', 'course', 'pickup_date', 'pickup_time', 'return_date',
                  'lesson_date', 'lesson_start_time', 'lesson_end_time', 'other_notes')
        # widgets = {'order': forms.HiddenInput()}
