from django.db import models
from django.conf import settings


############################################################################
# Class Model(s)
############################################################################
from django.db.models import Q

from users.models import CustomUser


class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher',
        null=False
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)


class CourseMember(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    course_member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='course_member',
        null=False
    )


class CourseComplete:
    course = Course()
    members = []
    orders = []


############################################################################
# Material Inventory Model(s)
############################################################################
class Item(models.Model):
    CATEGORY = (
        ('MATH', 'Mathematics'),
        ('CHEM', 'Chemistry'),
        ('BIO', 'Biology'),
        ('HOUSE', 'Household'),
        ('CRAFT', 'Craft'),
        ('PHYS', 'Physics'),
        ('TOY', 'Toy'),
        ('TECH', 'Tech')
    )
    item = models.CharField(max_length=50)
    category = models.CharField(max_length=5, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)


############################################################################
# Order Model(s)
############################################################################
class Order(models.Model):
    number = models.IntegerField(primary_key=True)
    STATUS = {
        (0, 'ASSIGNED'),
        (1, 'STARTED'),
        (2, 'PLACED'),
        (3, 'UPDATED'),
        (4, 'FILLED'),
        (5, 'SELF-FILLED'),
        (6, 'OUT'),
        (7, 'RETURNED'),
        (8, 'EMPTIED'),
        (9, 'DONE')
    }
    status = models.IntegerField(choices=STATUS, default=0)

    master_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # TODO: see if can fix to be based on classification number
        # limit_choices_to=({CustomUser.classification == 2}),
        limit_choices_to=Q(groups__name='Master Teacher'),
        related_name='master_teacher',
        null=True,
        blank=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True
    )

    trello_id = models.CharField(max_length=50, blank=True)

    # Pickup & Lesson information
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)

    # TODO: Abstract out to lesson table
    lesson_date = models.DateField(null=True, blank=True)
    lesson_start_time = models.TimeField(null=True, blank=True)
    lesson_end_time = models.TimeField(null=True, blank=True)

    other_notes = models.TextField(null=True, blank=True)


class OrderMember(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False
    )
    order_member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order_member',
        null=False
    )


class OrderContent(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    other_notes = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
    self_filled = models.BooleanField(default=False)


class OrderComplete:
    order = Order()
    status = ""
    members = []
    order_content = []
