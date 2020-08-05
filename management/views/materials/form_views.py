# Saves Form - Unlisted & Edit
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from management.forms import OrderDetailsForm
from materials.forms import UnlistedAddForm
from materials.models import Order, OrderContent


def save_generic_form(request, form, template_name, form_info):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    context.update(form_info)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def order_details_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderDetailsForm(request.POST, instance=order)
    else:
        form = OrderDetailsForm(instance=order)
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Edit Order Details",
               'cancel': "Cancel",
               'submit': "Update Order"}
    return save_generic_form(request, form, 'materials/includes/generic_modal_form.html', context)


def save_content_form(request, form, template_name, context):
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
            data['html_content_list'] = render_to_string('materials/includes/order_content_list.html', {
                'contents': contents,
            })
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Edit Item
def content_edit(request, pk):
    content = get_object_or_404(OrderContent, pk=pk)
    if request.method == 'POST':
        form = UnlistedAddForm(request.POST, instance=content)
    else:
        form = UnlistedAddForm(instance=content)
    context = {'form': form,
               'class': 'js-form-list',
               'action': request.path,
               'header': "Update Item",
               'cancel': "Cancel",
               'submit': "Update"}
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)


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

        data['html_content_list'] = render_to_string('materials/includes/order_content_list.html', {
            'contents': contents
        })
    else:
        context = {'content': content}
        data['html_form'] = render_to_string('materials/includes/order_content_delete.html', context, request=request)
    return JsonResponse(data)

