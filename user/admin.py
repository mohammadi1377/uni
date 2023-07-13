from django.contrib import admin
from .models import User, Student, Professor

admin.site.register(User)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_full_name', 'get_department', 'get_field', 'get_specialization']
    list_filter = ['field__department']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    ordering = ['user__last_name', 'user__first_name']

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Full Name'

    def get_department(self, obj):
        return obj.field.department

    get_department.short_description = 'Department'

    def get_field(self, obj):
        return obj.field.name

    get_field.short_description = 'Field'

    def get_specialization(self, obj):
        return obj.specialization.name if obj.specialization else '-'

    get_specialization.short_description = 'Specialization'


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_full_name', 'department', 'get_field', 'get_classes', 'get_specializations']
    list_filter = ['department', 'field']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    ordering = ['user__last_name', 'user__first_name']

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'Full Name'

    def get_field(self, obj):
        return obj.field.name if obj.field else '-'

    get_field.short_description = 'Field'

    def get_classes(self, obj):
        return obj.classes.name if obj.classes else '-'

    get_classes.short_description = 'Classes'

    def get_specializations(self, obj):
        return ', '.join(spec.name for spec in obj.specializations.all()) if obj.specializations.exists() else '-'

    get_specializations.short_description = 'Specializations'
