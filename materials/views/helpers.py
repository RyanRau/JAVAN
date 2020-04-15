from django.shortcuts import get_object_or_404

from users.models import CustomUser
from django.http import HttpResponseRedirect

from materials.models import Order, OrderMember, Course, CourseMember, CourseComplete


def get_orders(user):
    member_of = OrderMember.objects.filter(order_member=user)
    orders = []
    for order in member_of:
        orders.append(Order.objects.get(pk=order.order_id))

    return orders


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
    course.orders = Order.objects.filter(course_id=course_id)
    return course

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
