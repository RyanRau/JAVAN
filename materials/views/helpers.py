from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from users.models import CustomUser
from django.http import HttpResponseRedirect, HttpResponse

from materials.models import *


############################################################################
# Ajax
def item_list(request):
    items = Item.objects.all()

    query = request.GET.get("query")
    checks = request.GET.getlist("category[]")

    items = items.filter(Q(item__icontains=query) | Q(description__icontains=query))

    if checks:
        items = items.filter(category__in=checks)

    context = {
        'items': items,
    }
    html = render(request, "materials/includes/item_list.html", context=context)
    return HttpResponse(html)


############################################################################
# Order
def get_orders(user):
    member_of = OrderMember.objects.filter(order_member=user)
    orders = []
    for order in member_of:
        orders.append(Order.objects.get(pk=order.order_id))

    return orders


def get_order_status(status_number):
    statuses = ["ASSIGNED", "STARTED", "PLACED", "UPDATED",
                "FILLED", "SELF-FILLED", "OUT", "RETURNED", "EMPTIED", "DONE"]
    return statuses[status_number]


def get_order_members(order_id):
    members = []
    for m in OrderMember.objects.filter(order=order_id):
        members.append(m)

    return members


def get_complete_order(order_id):
    order = OrderComplete()

    order.order = get_object_or_404(Order, pk=order_id)
    order.status = str(get_order_status(order.order.status))

    members = OrderMember.objects.filter(order=order_id)
    order.members = []
    for member in members:
        order.members.append(member.order_member)

    order.order_content = OrderContent.objects.filter(order=order_id)
    return order


def get_responsible_orders(user):
    orders = Order.objects.filter(master_teacher=user)

    responsible_orders = []

    for order in orders:
        tmp_order = get_complete_order(order.pk)
        if user not in tmp_order.members:
            responsible_orders.append(get_complete_order(order.pk))

    return responsible_orders


############################################################################
# Courses
# Given orders, will return a list of the corresponding courses
def get_corresponding_courses(orders):
    courses = []
    for order in orders:
        courses.append(Course.objects.get(pk=order.course))
    return courses


def get_taught_course(user):
    courses = Course.objects.filter(teacher=user)
    return courses


def get_complete_course(course_id):
    course = CourseComplete()

    course.course = get_object_or_404(Course, pk=course_id)

    members = CourseMember.objects.filter(course_id=course_id)
    course.members = []
    for member in members:
        course.members.append(CustomUser.objects.get(pk=member.id))

    orders = Order.objects.filter(course=course.course)
    course.orders = []
    for order in orders:
        course.orders.append(get_complete_order(order.pk))

    return course


############################################################################
# Misc
# Checks if password needs to be changed
def password_check(function):
    def _function(request, *args, **kwargs):
        custom_user = CustomUser.objects.get(email=request.user.email)
        if custom_user.forcePasswordChange:
            return HttpResponseRedirect('/users/password/')
        return function(request, *args, **kwargs)
    return _function


# Add request and user status to context
def base_context(request):
    view = request.path_info

    context = {
        'view': view,
        'request': request,
    }
    return context
