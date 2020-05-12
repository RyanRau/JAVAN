from django.contrib.auth.decorators import login_required
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
    order = get_object_or_404(Order, pk=pk)

    context = base_context(request)
    context.update({
        'order': order,
    })
    return render(request, "./materials/order-view.html", context)
