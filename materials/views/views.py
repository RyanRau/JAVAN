from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponse, get_object_or_404
from materials.models import Order, OrderMember

from .helpers import *


# .../materials/
@login_required(login_url='/users/login/')
def index(request):
    orders = get_orders(request.user)
    complete_orders = []
    for order in orders:
        complete_orders.append(get_complete_order(order.number))

    # TODO: Add views for staff and teachers
    #         (0, "Student"),
    #         (1, "Mentor"),
    #         (2, "Work Study"),
    #         (3, "Master Teacher"),
    #         (4, "Admin"),

    if request.user.classification >= 3:
        elevated = True
        responsible_orders = get_responsible_orders(request.user)

        taught_courses = get_taught_course(request.user)
        taught_courses_complete = []

        for course in taught_courses:
            taught_courses_complete.append(get_complete_course(course.pk))

    else:
        elevated = False



        x = request.user.classification
        orders = get_orders(request.user)
        # courses = get_corresponding_courses(orders)
        # combined = zip(orders, courses)

    context = base_context(request)
    context.update({
        'complete_orders': complete_orders,
        'isElevated': elevated,
        'courses': taught_courses_complete,
    })
    return render(request, "./materials/index.html", context)


# .../materials/order/<int:id>
# pk: Order
@login_required(login_url='/users/login/')
def order_view(request, pk):
    request.session['order_number'] = pk

    # Get order details & items
    complete_order = get_complete_order(pk)
    items = Item.objects.all()

    context = base_context(request)
    context.update({
        'items': items,
        'contents': complete_order.order_content,
        'order': complete_order.order,
        'flag': 0
    })
    return render(request, "./materials/order_view.html", context)


# .../materials/order/<int:id>/review
# pk: Order
@login_required(login_url='/users/login/')
def order_review(request, pk):
    # Get order details
    complete_order = get_complete_order(pk)

    # if not is_permitted(request.user, order):
    #     return render(request, 'framework/denied.html')

    context = base_context(request)
    context.update({
        'order': complete_order.order,
        'contents': complete_order.order_content,
        # 'canSelfFill': canSelfFill
    })
    return render(request, 'materials/order_review.html', context)


def browse_items(request):
    items = Item.objects.all()

    context = base_context(request)
    context.update({
        'items': items,
    })
    return render(request, "./materials/browse_items.html", context)
