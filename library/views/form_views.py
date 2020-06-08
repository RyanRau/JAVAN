# Saves Form - Unlisted & Edit
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.db.models import F

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
            if book.quantity == 0:
                error = 'There are no available copies of this book at the moment.'
                context = {'book': book, 'form': form, 'error': error}
                data['html_form'] = render_to_string('library/book_details.html', context,
                                                     request=request)
            else:
                user = request.user
                model = Checkout()
                model.book = book
                model.user_checkout = user
                model.checkout_date = form.cleaned_data.get('checkout_date')
                model.save()
                book.quantity = book.quantity - 1
                book.save()
                data['form_is_valid'] = True
                ## RYAN: this bit gets the checked out stuff and the js file uses this to fill the list on the right col
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
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def save_add_form(request, form, template_name, context):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            isbn = form.cleaned_data.get('isbn')
            qs = Book.objects.filter(isbn=isbn)
            if qs.exists():
                error = 'ISBN exists'
                print(error)
                ## PROBLEM
                # trying to alert cant add bc duplicate, not working yet
                context = {
                    'form': form,
                    'class': 'js-form-list',
                    'action': request.path,
                    'header': "Add Book",
                    'cancel': "Cancel",
                    'submit': "Add Book",
                    'field.error': error
                }
                context.update(context)
            else:
                print('valid form')
                form.save()
                data['form_is_valid'] = True
        else:
            print('invlaid form')
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = AddBookForm(request.POST, instance=book)
    else:
        form = AddBookForm(instance=book)

    ## RYAN: js-form/js-form-listed refers to class that triggers js ajax call
    ## RYAN: js-form: no updating content js-form-list: update content
    context = {
        'form': form,
        'class': 'js-form-list',
        'action': request.path,
        'header': "Edit Book",
        'cancel': "Cancel",
        'submit': "Update"
    }
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)

# TODO: fix errors and problems with this
# TODO: also clean up this page and all the others
def add_book(request):
    if request.method == 'POST':
        print('post add_book')
        form = AddBookForm(request.POST)
    else:
        print('add_book else')
        form = AddBookForm()
    context = {'form': form,
               'class': 'js-form-list',
               'action': request.path,
               'header': "Add Book",
               'cancel': "Cancel",
               'submit': "Add Book"}
    return save_add_form(request, form, 'materials/includes/generic_modal_form.html', context)


# TODO: maybe find out how to morph with normal book details ?
# since it is very similar
def new_checkout(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = NewCheckoutForm(request.POST)
        if form.is_valid():
            print('checkout valid')
            if book.quantity == 0:
                error = 'There are no available copies of this book at the moment.'
                context = {'book': book, 'form': form, 'error': error}
                data['html_form'] = render_to_string('library/new_checkout.html', context,
                                                     request=request)
            else:
                model = Checkout()
                model.book = book
                model.user_checkout = form.cleaned_data.get('user_checkout')
                model.checkout_date = form.cleaned_data.get('checkout_date')
                model.save()
                book.quantity = book.quantity - 1
                book.save()
                data['form_is_valid'] = True
        else:
            error = 'An error has occurred, please refresh the page and try again.'
            context = {'book': book, 'form': form, 'error': error}
            data['html_form'] = render_to_string('library/new_checkout.html', context,
                                                 request=request)
    else:
        form = NewCheckoutForm()
        context = {'book': book, 'form': form}
        data['html_form'] = render_to_string('library/new_checkout.html', context, request=request)
    return JsonResponse(data)
