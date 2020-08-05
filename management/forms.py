from django import forms

from materials.models import Order, Item


# TODO: make more independent from materials
class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status', 'master_teacher', 'course', 'pickup_date', 'pickup_time', 'return_date',
                  'lesson_date', 'lesson_start_time', 'lesson_end_time', 'other_notes')
        # widgets = {'order': forms.HiddenInput()}


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item', 'category', 'description', 'location')