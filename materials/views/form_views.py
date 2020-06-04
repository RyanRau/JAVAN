from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from materials.forms import *
from materials.models import *
from materials.views.helpers import *


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
               'class': 'js-form',
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
    return pickup_update_save(request, pk, form, 'materials/includes/generic_modal_form.html')


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
            data['html_content_list'] = render_to_string('materials/includes/order_content_list.html', {
                'contents': content
            })
        else:
            error = 'An error has occurred, please refresh the page and try again.'
            context = {'book': item, 'form': form, 'error': error}
            data['html_form'] = render_to_string('materials/includes/listed_item_add.html', context,
                                                 request=request)
    else:
        form = ListedAddForm()
        context = {'item': item, 'form': form}
        data['html_form'] = render_to_string('materials/includes/listed_item_add.html', context, request=request)
    return JsonResponse(data)


# Saves Form - Unlisted & Edit
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


# Unlisted Add
def unlisted_add(request):
    if request.method == 'POST':
        form = UnlistedAddForm(request.POST)
    else:
        form = UnlistedAddForm()
    context = {'form': form,
               'class': 'js-form-list',
               'action': request.path,
               'header': "Add Unlisted Item",
               'cancel': "Cancel",
               'submit': "Add Item"}
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)


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


########################################################################################
# Item add/edit/delete form
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


def item_add(request):
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
    else:
        form = ItemAddForm()
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Create New Item",
               'cancel': "Cancel",
               'submit': "Create Item"}
    return save_generic_form(request, form, 'materials/includes/generic_modal_form.html', context)


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemAddForm(request.POST, instance=item)
    else:
        form = ItemAddForm(instance=item)
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Update Item",
               'cancel': "Cancel",
               'submit': "Update item"}
    return save_generic_form(request, form, 'materials/includes/generic_modal_form.html', context)





########################################################################################
# Course related forms
def course_create(request):
    x = 1


def course_order_save(request, form, course_pk=None):
    data = dict()
    if request.method == 'POST':
        # Creates new order
        if course_pk:
            try:
                Order.objects.get(pk=request.POST['order_number'])
                orderExists = True
            except:
                orderExists = False

            if orderExists:
                form.add_error('order_number', 'This Order number has already been taken')
                data['form_is_valid'] = False
            else:
                data['form_is_valid'] = True

                # Creates order
                order = Order()
                order.number = request.POST['order_number']
                order.course_id = course_pk
                order.save()

        # Updates order
        else:
            order = Order.objects.get(pk=request.POST['order_number'])

            data['form_is_valid'] = True

            # Deletes members
            members = get_order_members(request.POST['order_number'])
            for member in members:
                OrderMember.objects.get(pk=member.pk).delete()

        # Creates member association
        students = dict(request.POST)['username']
        for student in students:
            order_member = OrderMember()
            order_member.order = order
            order_member.order_member = CustomUser.objects.get(pk=student)
            order_member.save()

    else:
        data['form_is_valid'] = False

    context = {
        'form': form,
        'action': request.path,
    }

    data['html_form'] = render_to_string('materials/includes/multiselect_form.html', context, request=request)
    return JsonResponse(data)


# pk: Order
def course_order_edit(request, pk):
    members = []
    for m in get_order_members(pk):
        members.append(m.order_member.pk)

    init_content = {
        'order_number': pk,
        'username': members
    }
    if request.method == 'POST':
        form = CourseOrderAdd(True, request.POST)
    else:
        form = CourseOrderAdd(True, initial=init_content)

    return course_order_save(request, form)


# pk: Course
def course_order_add(request, pk):
    if request.method == 'POST':
        form = CourseOrderAdd(False, request.POST)
    else:
        form = CourseOrderAdd(False)

    return course_order_save(request, form, pk)
