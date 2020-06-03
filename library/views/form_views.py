# Saves Form - Unlisted & Edit
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from library.forms import *
from library.models import *
from users.models import CustomUser


def save1_content_form(request, form, template_name, context):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Demo Form
def demo(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
    else:
        form = DemoForm()
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Demo Form",
               'cancel': "Cancel",
               'submit': "Submit"}
    return save1_content_form(request, form, 'library/includes/generic_modal_form.html', context)


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()

    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():

            user = request.user
            model = Checkout()
            model.book = book
            # book.quantity = book.quantity - 1
            model.user_checkout = user
            model.checkout_date = form.cleaned_data.get('checkout_date')
            model.save()

            data['form_is_valid'] = True

            content = Checkout.objects.filter(user_checkout=user)

            data['html_content_list'] = render_to_string('library/user_check_outs.html',
                                                         {'contents': content})
        #     some other stuff
        else:
            error = 'An error has occurred, please refresh the page and try again.'
            context = {'book': book, 'form': form, 'error': error}
            data['html_form'] = render_to_string('library/book_details.html', context,
                                                 request=request)

    else:
        form = DemoForm()
        context = {'book': book, 'form': form}
        data['html_form'] = render_to_string('library/book_details.html', context, request=request)
    return JsonResponse(data)


def save_content_form(request, form, template_name, context):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            qs = Book.objects.filter(isbn=form.cleaned_data.get('isbn'))
            if qs.exists():
                data['form_is_valid'] = False
            else:
                form.save()
                data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def edit_book(request, pk):
    print('called')
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = AddBookForm(request.POST, instance=book)
    else:
        form = AddBookForm(instance=book)
    context = {
        'form': form,
        'class': 'js-form',
        'action': request.path,
        'header': "Edit Book",
        'cancel': "Cancel",
        'submit': "Update"
    }
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
    else:
        form = AddBookForm()
    context = {'form': form,
               'class': 'js-form',
               'action': request.path,
               'header': "Add Book",
               'cancel': "Cancel",
               'submit': "Add Book"}
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)
