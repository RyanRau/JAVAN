from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404

from materials.models import *


def getUpcomingPickUps():
    orders = Order.objects.all()

    today = datetime.now()
    weekFromNow = datetime.now() + timedelta(days=7)

    upcoming_orders = []

    for order in orders:
        if today <= order.pickup_date <= weekFromNow:
            upcoming_orders.append(order)

    return upcoming_orders


def getOverdueReturns():
    orders = Order.objects.all()

    overdue_orders = []

    for order in orders:
        if order.return_date < datetime.now():
            overdue_orders.append(order)

    return overdue_orders


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


############################################################################
# Courses
# Given orders, will return a list of the corresponding courses
def get_corresponding_courses(orders):
    courses = []
    for order in orders:
        courses.append(Course.objects.get(pk=order.course))
    return courses

def get_course_members(course_id):
    members = []
    for m in CourseMember.objects.filter(course=course_id):
        members.append(m)

    return members


def get_taught_course(user):
    courses = Course.objects.filter(teacher=user)
    return courses


def get_complete_course(course_id):
    course = CourseComplete()

    course.course = get_object_or_404(Course, pk=course_id)

    # members = CourseMember.objects.filter(course_id=course_id)
    course.members = get_course_members(course_id)
    # for member in members:
    #     course.members.append(CustomUser.objects.get(pk=member.id))

    orders = Order.objects.filter(course=course.course)
    course.orders = []
    for order in orders:
        course.orders.append(get_complete_order(order.pk))

    return course