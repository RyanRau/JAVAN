from django.contrib import admin

from materials.models import Order, OrderMember, OrderContent, Course, CourseMember, Item


############################################################################
# Order Models
############################################################################
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'trello_id', 'master_teacher', 'course',
                    'course', 'pickup_date', 'pickup_time')


class OrderMemberAdmin(admin.ModelAdmin):
    list_display = ('order', 'order_member')


class OrderContentAdmin(admin.ModelAdmin):
    list_display = ('order', 'quantity', 'item', 'location')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderMember, OrderMemberAdmin)
admin.site.register(OrderContent, OrderContentAdmin)


############################################################################
# Course Models
############################################################################
class CourseAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'code', 'name')


class CourseMemberAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_member')


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMember, CourseMemberAdmin)


############################################################################
# Inventory Models
############################################################################
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'category', 'location')


admin.site.register(Item, ItemAdmin)
