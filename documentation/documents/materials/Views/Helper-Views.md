# Helpers.py
---
materials/views/helpers.py contain helper function for various purposes.

- [OrderComplete](#ordercomplete)
- [CourseComplete](#coursecomplete)



<a name="ordercomplete"></a>
### OrderComplete helper functions
---
Phasellus non semper magna. Fusce faucibus risus a arcu mollis vehicula. Phasellus nec quam non est euismod euismod et quis lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin vehicula in ante eu ornare. Nunc at dapibus enim, eu aliquam turpis. Suspendisse sed turpis massa. Ut sollicitudin, justo non faucibus feugiat, ipsum lacus faucibus massa, eget accumsan turpis eros non mauris. Nulla arcu odio, ultricies at magna quis, eleifend ornare ex. Duis at arcu lectus. Ut tristique dignissim dui quis posuere. Curabitur a ornare lorem, nec aliquam nisi.

Morbi egestas auctor nibh, efficitur pharetra justo tincidunt non. Nam risus orci, volutpat eu consectetur vitae, consequat quis urna. In hac habitasse platea dictumst. Curabitur at nisl non sem volutpat porttitor eget eget lacus. Sed dapibus malesuada risus, a tincidunt ipsum imperdiet id. Pellentesque consectetur, elit quis venenatis sodales, diam felis fermentum odio, ac rutrum nulla lectus vitae nulla. Maecenas vitae orci ante. Sed sapien sapien, tempor in purus a, placerat euismod lectus. Nullam enim sem, posuere sed ante a, auctor rutrum leo. Donec consectetur felis id odio vulputate, quis faucibus lacus ullamcorper. Vivamus vitae orci vitae massa hendrerit tincidunt consectetur id elit. Morbi lorem erat, gravida lobortis mollis et, feugiat eget urna. In vel vulputate augue. Aliquam convallis leo non diam rutrum facilisis.

Phasellus luctus eros in elei
vPhasellus non semper magna. Fusce faucibus risus a arcu mollis vehicula. Phasellus nec quam non est euismod euismod et quis lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin vehicula in ante eu ornare. Nunc at dapibus enim, eu aliquam turpis. Suspendisse sed turpis massa. Ut sollicitudin, justo non faucibus feugiat, ipsum lacus faucibus massa, eget accumsan turpis eros non mauris. Nulla arcu odio, ultricies at magna quis, eleifend ornare ex. Duis at arcu lectus. Ut tristique dignissim dui quis posuere. Curabitur a ornare lorem, nec aliquam nisi.

Morbi egestas auctor nibh, efficitur pharetra justo tincidunt non. Nam risus orci, volutpat eu consectetur vitae, consequat quis urna. In hac habitasse platea dictumst. Curabitur at nisl non sem volutpat porttitor eget eget lacus. Sed dapibus malesuada risus, a tincidunt ipsum imperdiet id. Pellentesque consectetur, elit quis venenatis sodales, diam felis fermentum odio, ac rutrum nulla lectus vitae nulla. Maecenas vitae orci ante. Sed sapien sapien, tempor in purus a, placerat euismod lectus. Nullam enim sem, posuere sed ante a, auctor rutrum leo. Donec consectetur felis id odio vulputate, quis faucibus lacus ullamcorper. Vivamus vitae orci vitae massa hendrerit tincidunt consectetur id elit. Morbi lorem erat, gravida lobortis mollis et, feugiat eget urna. In vel vulputate augue. Aliquam convallis leo non diam rutrum facilisis.

Phasellus luctus eros in elei

<a name="coursecomplete"></a>
### CourseComplete helper functions
---
#### - get_complete_course(course_id)

Given course_id get_complete_course() will return a CourseComplete object containing:

- course
- members (list of users)
- orders  (list CompleteOrder objects)

##### *Code*
```python
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
```



