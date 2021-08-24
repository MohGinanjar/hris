from django.contrib import admin
from .models import (Users, Employee, Salary, EmployeeForUpdate)
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin, ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter


class UsersSalaryAdmin(admin.ModelAdmin):
    search_fields = ['pin','name']
    list_display = ('pin','name','phone',)
    list_filter = ('created_at',)
    list_per_page = 10

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['employee_id__id','employee_phone','employee_id__name','employee_id__pin', 'email']
    list_select_related = ['employee']
    list_display = ('employee','employee_phone','employee_simcard','email')
    list_filter = ('created_at',)
    autocomplete_fields =[
        'employee'
    ]

class EmployeeUpdateAdmin(admin.ModelAdmin):
    search_fields = ['employee_id__id','employee_phone','employee_id__name','employee_id__pin', 'email']
    list_display = ('employee_id','employee_phone','employee_simcard','email')
    list_filter = ('created_at',)
    autocomplete_fields =[
        'employee_id'
    ]
    # def get_form(self, request, obj=None, **kwargs):
    #     request.current_object = obj
    #     return super(CustomModelAdmin, self).get_form(request, obj, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):

    #     if db_field.name == 'employee':
    #         instance = request.current_object
    #         if instance.brand and instance.memory_size:
    #                 filtered_qs=StandardProductWithMemorySize.objects.filter(
    #                     product__brand=instance.brand,
    #                     memory_size=instance.memory_size
    #                 )
    #                 kwargs['queryset'] = filtered_qs
    #                 db = kwargs.get('using')
    #                 kwargs['widget'] = AutocompleteSelect(db_field.remote_field, self.admin_site)
    #     return super(
    #         CustomModelAdmin, self
    #     ).formfield_for_foreignkey(db_field, request, **kwargs)
    list_per_page = 10

admin.site.site_header = 'HRIS Admin Hino Panel'

class SalaryAdmin(admin.ModelAdmin):
    search_fields = ['employee_pin','employee_name','employee_level',]
    list_display = ('employee_pin','employee_name','employee_level',)
    list_filter = ('created_at',)
    list_per_page = 10


admin.site.register(Users, UsersSalaryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(EmployeeForUpdate, EmployeeUpdateAdmin)