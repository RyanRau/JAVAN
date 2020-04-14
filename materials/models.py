from django.db import models
from django.conf import settings


############################################################################
# Class Model(s)
############################################################################
class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher',
        null=False
    )


class ClassMember(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
        null=False
    )


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
