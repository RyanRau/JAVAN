from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .helpers import *

from materials.models import Order


def order_search(request):
    # Search Orders by number, course, students, master  teacher

    query = request.GET.get("query")
    search_terms = query.split(',')

    complete_orders = []
    for order in Order.objects.order_by('number'):
        complete_orders.append(get_complete_order(order.pk))

    for term in search_terms:
        term = term.strip()
        # see if any are int for order number
        try:
            number = int(term)
            for i, complete_order in enumerate(complete_orders):
                if complete_order.order.pk is not number:
                    complete_orders[i] = None
        except:
            # Check for students, course
            for i, complete_order in enumerate(complete_orders):
                if complete_order is not None:
                    include = False
                    for member in complete_order.members:
                        if term.lower() in member.first_name.lower() + ' ' + member.last_name.lower():
                            include = True
                    if complete_order.order.course is not None:
                        if term.lower() in complete_order.order.course.name.lower():
                            include = True
                    if term.lower() in complete_order.status.lower():
                        include = True
                if not include:
                    complete_orders[i] = None

    sorted_list = []
    for complete_order in complete_orders:
        if complete_order is not None:
            sorted_list.append(complete_order)

    context = {
        'orders': sorted_list,
    }
    html = render(request, "management/orders/includes/order_search.html", context=context)
    return HttpResponse(html)

def course_search(request):
    query = request.GET.get("query")
    search_terms = query.split(',')

    complete_courses = []
    for course in Course.objects.all():
        complete_courses.append(get_complete_course(course.pk))
    #
    # for term in search_terms:
    #     term = term.strip()
    #     # see if any are int for order number
    #     try:
    #         number = int(term)
    #         for i, complete_order in enumerate(complete_orders):
    #             if complete_order.order.pk is not number:
    #                 complete_orders[i] = None
    #     except:
    #         # Check for students, course
    #         for i, complete_order in enumerate(complete_orders):
    #             if complete_order is not None:
    #                 include = False
    #                 for member in complete_order.members:
    #                     if term.lower() in member.first_name.lower() + ' ' + member.last_name.lower():
    #                         include = True
    #                 if complete_order.order.course is not None:
    #                     if term.lower() in complete_order.order.course.name.lower():
    #                         include = True
    #                 if term.lower() in complete_order.status.lower():
    #                     include = True
    #             if not include:
    #                 complete_orders[i] = None
    #
    # sorted_list = []
    # for complete_order in complete_orders:
    #     if complete_order is not None:
    #         sorted_list.append(complete_order)
    print(len(complete_courses))

    context = {
        'complete_courses': complete_courses,
    }
    html = render(request, "management/courses/includes/course_search.html", context=context)
    return HttpResponse(html)