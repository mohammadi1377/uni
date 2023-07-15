from django.contrib import admin
from .models import Department, Course, Room, Class, Field, Specialization


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department']
    list_filter = ['department']
    search_fields = ['name', 'code', 'department__name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']
    search_fields = ['name']


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['course', 'room', 'department', 'start_time', 'end_time', 'days_of_week']
    list_filter = ['department', 'days_of_week']
    search_fields = ['course__name', 'room__name', 'department__name']
    ordering = ['start_time']


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    list_filter = ['department']
    search_fields = ['name', 'department__name']


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name', 'field']
    list_filter = ['field__department']
    search_fields = ['name', 'field__name']


admin.site.site_header = "University Administration"
admin.site.index_title = "Manage University"
admin.site.site_title = "University Admin Panel"
