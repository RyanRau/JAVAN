from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from materials.forms import *
from materials.models import *


########################################################################################
# Pickup Information
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


########################################################################################
# Listed & Unlisted add/edit/delete forms
def listed_add(request, pk):
    item = get_object_or_404(Item, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = ListedAddForm(request.POST)
        if form.is_valid():
            order_number = request.session['order_number']
            order = get_object_or_404(Order, pk=order_number)

            model = OrderContent()
            model.order = order
            model.item = item.item
            model.location = item.location
            model.quantity = form.cleaned_data.get('quantity')
            model.other_notes = form.cleaned_data.get('other_notes')
            model.self_filled = form.cleaned_data.get('self_filled')
            model.save()

            data['form_is_valid'] = True
            content = OrderContent.objects.filter(order=order)
            data['html_content_list'] = render_to_string('materials/includes/order_content.html', {
                'contents': content
            })
        else:
            error = 'An error has occurred, please refresh the page and try again.'
            context = {'book': item, 'form': form, 'error': error}
            data['html_form'] = render_to_string('materials/includes/listed_add.html', context,
                                                 request=request)
    else:
        form = ListedAddForm()
        context = {'item': item, 'form': form}
        data['html_form'] = render_to_string('materials/includes/listed_add.html', context, request=request)
    return JsonResponse(data)


# Saves Form - Unlisted & Edit
def save_content_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            order_number = request.session['order_number']
            order = get_object_or_404(Order, pk=order_number)

            copy = form.save(commit=False)
            copy.order = order
            copy.location = 'UNLISTED'
            form.save()

            data['form_is_valid'] = True

            contents = OrderContent.objects.filter(order=order)
            data['html_content_list'] = render_to_string('materials/includes/order_content.html', {
                'contents': contents,
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Unlisted Add
def unlisted_add(request):
    if request.method == 'POST':
        form = UnlistedAddForm(request.POST)
    else:
        form = UnlistedAddForm()
    return save_content_form(request, form, 'materials/includes/partial_unlisted_add.html')


# Edit Item
def content_edit(request, pk):
    content = get_object_or_404(OrderContent, pk=pk)
    if request.method == 'POST':
        form = UnlistedAddForm(request.POST, instance=content)
    else:
        form = UnlistedAddForm(instance=content)
    return save_content_form(request, form, 'materials/includes/partial_content_edit.html')


# Delete Item
def content_delete(request, pk):
    content = get_object_or_404(OrderContent, pk=pk)
    data = dict()
    if request.method == 'POST':
        content.delete()
        data['form_is_valid'] = True
        order_number = request.session['order_number']
        order = get_object_or_404(Order, pk=order_number)
        contents = OrderContent.objects.filter(order=order)

        data['html_content_list'] = render_to_string('materials/includes/order_content.html', {
            'contents': contents,
        })
    else:
        context = {'content': content}
        data['html_form'] = render_to_string('materials/includes/partial_content_delete.html', context, request=request)
    return JsonResponse(data)