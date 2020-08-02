from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .materials.helpers import *

from materials.models import Order, OrderContent, OrderMember, OrderComplete


@login_required(login_url='/users/login/')
def index(request):
    context = {}
    return render(request, "./management/index.html", context)


@login_required(login_url='/users/login/')
def order_list(request):
    orders = []

    for order in Order.objects.all():
        orders.append(get_complete_order(order.pk))

    context = {
        'orders': orders
    }
    return render(request, "./management/orders/order_list.html", context)


@login_required(login_url='/users/login/')
def order_view(request, pk):
    complete_order = get_complete_order(pk)

    request.session['order_number'] = pk

    context = {
        'order': complete_order.order,
        'status': complete_order.status,
        'contents': complete_order.order_content,
        'members': complete_order.members
    }
    return render(request, "./management/orders/order_view.html", context)


@login_required(login_url='/users/login/')
def course_list(request):
    courses = []

    for course in Course.objects.all():
        courses.append(get_complete_course(course.pk))

    context = {
        'course': course
    }
    return render(request, "./management/courses/course_list.html", context)


@login_required(login_url='/users/login/')
def course_view(request, pk):
    complete_course = get_complete_course(pk)

    context = {
        'course': complete_course.course,
        'members': complete_course.members
    }
    return render(request, "./management/courses/course_view.html", context)
