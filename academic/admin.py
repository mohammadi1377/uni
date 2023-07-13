from django.contrib import admin
from .models import Department, Course, Room, Class, Field, Specialization

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Field)
admin.site.register(Specialization)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['course', 'room', 'department', 'start_time', 'end_time', 'days_of_week']
    list_filter = ['course', 'room', 'department']
    search_fields = ['course__name', 'room__name', 'department__name']
    ordering = ['start_time']
