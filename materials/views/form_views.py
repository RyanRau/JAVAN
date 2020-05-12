########################################################################################
# Handles Pickup Information Forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from materials.forms import *
from materials.models import *


def pickup_update_save(request, pk, form, template_name):
    data = dict()
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        if form.is_valid():
            # First time pickup info change
            if order.status == 0:
                copy = form.save(commit=False)
                copy.status = 1
                form.save()

                data['form_is_valid'] = True
                data['redirect_url'] = 'order/' + str(pk)
            # Update in review order page
            else:
                form.save()
                data['form_is_valid'] = True
                data['redirect_url'] = '/materials/order/' + str(pk) + '/review'
        else:
            data['form_is_valid'] = False
    context = {'form': form,
               'action': request.path,
               'header': "Pick-up Information",
               'cancel': "Cancel",
               'submit': "Submit"}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def pickup_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = PickupForm(request.POST, instance=order)
    else:
        form = PickupForm(instance=order)
    return pickup_update_save(request, pk, form, 'materials/includes/generic_form.html')
