# Saves Form - Unlisted & Edit
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.db.models import F

from library.forms import *
from library.models import *
from library.trello import create_and_populate_chk
from users.models import CustomUser


# Book Details and Checkout for logged in user
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
                save_checkout(request, form, model, book, user)
                data['form_is_valid'] = True
                ## RYAN: this bit gets the checked out stuff and the js file uses this to fill the list on the right col
                content = Checkout.objects.filter(user_checkout=user)

                data['html_content_list'] = render_to_string('library/user_check_outs.html',
                                                             {'contents': content})
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


# Edit book in catalog
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


# TODO: might add more checkout details
# Edit checkout
def edit_checkout(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    if request.method == 'POST':
        form = EditCheckoutForm(request.POST, instance=checkout)
    else:
        form = EditCheckoutForm(instance=checkout)

    context = {
        'form': form,
        'class': 'js-form-list',
        'action': request.path,
        'header': "Edit Checkout",
        'cancel': "Cancel",
        'submit': "Update"
    }
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)


# TODO: fix errors and problems with this
# Add book to catalog
def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
    else:
        form = AddBookForm()
    context = {'form': form,
               'class': 'js-form-list',
               'action': request.path,
               'header': "Add Book",
               'cancel': "Cancel",
               'submit': "Add Book"}
    return save_content_form(request, form, 'materials/includes/generic_modal_form.html', context)


# New Checkout for work study to make for others
def new_checkout(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = NewCheckoutForm(request.POST)
        if form.is_valid():
            if book.quantity == 0:
                error = 'There are no available copies of this book at the moment.'
                context = {'book': book, 'form': form, 'error': error}
                data['html_form'] = render_to_string('library/new_checkout.html', context,
                                                     request=request)
            else:
                user = form.cleaned_data.get('user_checkout')
                model = Checkout()
                save_checkout(request, form, model, book, user)
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


# TODO: the saving twice thing isnt great probably
# Saving checkout model
def save_checkout(request, form, model, book, user):
    model.book = book
    model.user_checkout = user
    model.checkout_date = form.cleaned_data.get('checkout_date')
    model.return_date = form.cleaned_data.get('return_date')
    model.save()

    card_id = create_and_populate_chk(model.id, url=request.META['HTTP_HOST'])
    model.trello_id = card_id
    model.save()
    book.quantity = book.quantity - 1
    book.save()
