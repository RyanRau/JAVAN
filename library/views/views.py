from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from library.models import Book, Checkout
from library.trello import archive_chk
from materials.forms import *


@login_required(login_url='/users/login/')
def index(request):
    books = Book.objects.all()

    ## RYAN: Need to init the checked out books list...
    ## RYAN: since its an include you just need to pass the content along in the context
    content = Checkout.objects.filter(user_checkout=request.user)

    context = base_context(request)
    context.update({
        'books': books,
        'contents': content
    })
    return render(request, "./library/index.html", context)


# TODO: maybe search
def all_checkouts(request):
    checkouts = Checkout.objects.all()

    context = base_context(request)
    context.update({
        'checkouts': checkouts,
    })
    return render(request, "./library/all_checkouts.html", context)


def delete_checkout(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    book = checkout.book
    archive_chk(pk)
    checkout.delete()
    book.quantity = book.quantity + 1
    book.save()
    checkouts = Checkout.objects.all()

    context = base_context(request)
    context.update({
        'checkouts': checkouts,
    })
    return render(request, "./library/all_checkouts.html", context)


# Add request and user status to context
def base_context(request):
    view = request.path_info

    context = {
        'view': view,
        'request': request,
    }
    return context


def book_list(request):
    books = Book.objects.all()

    query = request.GET.get("query")

    books = books.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query) |
                         Q(category__icontains=query))

    context = {
        'books': books,
    }
    html = render(request, "library/book_list.html", context=context)
    return HttpResponse(html)
