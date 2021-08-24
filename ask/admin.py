from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Profile, FamilyMember
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin, ImportExportModelAdmin
# Register your models here.
class MasterVaksin(ImportExportModelAdmin):
    list_filter = [('created_date', DateRangeFilter),'created_date','div', 'ask_3']
    search_fields = ['nik','name',]
    list_display = ('nik','name','no_ktp','div','ask_1','ask_2','ask_3','ask_4')
    list_per_page = 15

admin.site.register(Profile, MasterVaksin)


class MasterVaksinMember(ImportExportModelAdmin):
    list_filter = [('created_date', DateRangeFilter),'created_date', 'ask_3']
    search_fields = ['name','nik_emp']
    list_display = ('nik_emp','name','no_ktp','age','ask_1','ask_2','ask_3','ask_4')
    list_per_page = 15
    

admin.site.register(FamilyMember, MasterVaksinMember)