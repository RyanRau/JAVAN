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

    courses = []
    for course in get_taught_course(request.user):
        courses.append(get_complete_course(course.id))

    # TODO: Add views for staff and teachers
    if request.user.classification >= 3:
        x = 1
    else:
        x = request.user.classification
        orders = get_orders(request.user)
        # courses = get_corresponding_courses(orders)
        # combined = zip(orders, courses)

    context = base_context(request)
    context.update({
        'complete_orders': complete_orders,

    })
    return render(request, "./materials/index.html", context)


# .../materials/order/<int:id>
@login_required(login_url='/users/login/')
def order_view(request, pk):
    request.session['order_number'] = pk

    # Get order details & items
    complete_order = get_complete_order(pk)
    items = Item.objects.all()

    # TODO: make dynamic with ajax
    # Search box: filters items
    query = request.GET.get("q")
    if query:
        items = items.filter(Q(item__icontains=query) | Q(description__icontains=query))

    context = base_context(request)
    context.update({
        'items': items,
        'contents': complete_order.order_content,
        'order': complete_order.order,
    })
    return render(request, "./materials/order_view.html", context)


# .../materials/order/<int:id>/review
@login_required(login_url='/users/login/')
def order_review(request, pk):
    # Get order details
    complete_order = get_complete_order(pk)

    # if not is_permitted(request.user, order):
    #     return render(request, 'framework/denied.html')


    # canSelfFill = can_self_fill(request.user)

    context = base_context(request)
    context.update({
        'order': complete_order.order,
        'contents': complete_order.order_content,
        # 'canSelfFill': canSelfFill
    })
    return render(request, 'materials/order_review.html', context)