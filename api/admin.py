from django.contrib import admin
from .models import (CoordinatUser, CoordinatOffice, WorkTime,
                    TimeView, WorkTasklist, InsurResult, 
                    Workingcalendar,WorkingcalendarCreate,MasterEmployee,
                    MasterDivision,MasterDepartment,Logbookheader)
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin, ImportExportModelAdmin
from import_export import resources
from .resources import *
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter


class TypeWork(admin.SimpleListFilter):
    title = 'type_work'
    parameter_name = 'type_work__in'

    
    def lookups(self, request, model_admin):
        # you can modify this part, this is less DRY approach.
        # P.S. assuming city_name is lowercase CharField
        return (
            ('WFH,WFT,AFH', 'WFH,WFT,AFH'),
            ('OH,HO,WFO', 'OH,HO,WFO'),
        )

    def queryset(self, request, queryset):
        if self.value() in ('WFH,WFT,AFH','OH,HO,WFO'):
            # filter if a choice selected
            return queryset.filter(type_work__in=self.value().split(','))
        # default for no filtering
        return queryset

    # def lookups(self, request, model_admin):
    #     # This is where you create filter options; we have two:
    #     return [
    #         ('WFH', 'WFH'),
    #         ('AFH', 'AFH'),
    #     ] 

    # def queryset(self, request, queryset):
    #         # This is where you process parameters selected by use via filter options:
    #     if self.value() == 'WFH':
    #         # Get websites that have at least one page.
    #         return queryset.distinct().filter(type_work__isnull=False)
    #     if self.value():
    #         # Get websites that don't have any pages.
    #         return queryset.distinct().filter(type_work__isnull=True)

class MasterTimeviewAdmin(ImportExportModelAdmin):
    list_filter = [('date', DateRangeFilter), TypeWork, 'date']
    search_fields = ['nik','name',]
    list_display = ('nik','name','date','time_in','time_out','type_work')
    list_per_page = 15



class MasterDeptAdmin(admin.ModelAdmin):
    search_fields = ['dept_id',]
    list_display = ('dept_id','dept_name','division_id',)
    list_filter = ('division_id','dept_name',)
    list_per_page = 15

class MasterDivisionAdmin(admin.ModelAdmin):
    search_fields = ['division_id',]
    list_display = ('division_id','division_name',)
    list_filter = ('division_id','division_name',)
    list_per_page = 25

class Inline(admin.TabularInline):
    model = CoordinatUser


class CordinatUserAdmin(ImportExportModelAdmin):
    search_fields = ['nik','name']
    list_display = ('nik','name','lat','long','address','office1')
    list_filter = ('time','office1',)
    list_per_page = 15


class CordinatOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ('title','latoffice','longoffice',)
    list_filter = ('title',)

class MasterEmployeeAdmin(ImportExportModelAdmin):
    search_fields = ['emp_no','emp_name']
    list_display = ('emp_no','emp_name','approverid1','approverid2','location_code','status_emp')
    list_filter = ('location_code','status_emp')

class LeaveHeaderAdmin(ImportExportModelAdmin):
    search_fields = ['ref_id',]
    list_display = ('ref_id','wk_type','from_dt','finish_dt','approver_1','approver_2','reason','in_time','out_time')
    list_filter = [('crt_dt', DateRangeFilter)]
    list_per_page = 10


@admin.register(InsurResult)
class PersonAdmin(ImportExportModelAdmin):
    resource_class  = InsuranceResource
    list_display = ("emp_no","comment","result_insur",)
    search_fields = ['emp_no','result_insur']
    list_filter = ('result_insur',)
    list_per_page = 10

@admin.register(Workingcalendar)
class WorkingCalenderAdmin(ImportExportModelAdmin):
    resource_class  = WorkingCalenderResource
    list_display = ("wk_day","wk_type","wk_desc","arriv_time","out_time","group_id","dy_name","yyyy","crt_dt","user_id",)
    search_fields = ["wk_day",]
    list_filter = ("yyyy","dy_name","wk_type","wk_desc","group_id","wk_desc",)
    list_per_page = 10

# class UserResource(resources.ModelResource):
#     class Meta:
#         model = User
#         fields = ('username','password','email','id', 'first_name',)

# class UserAdmin(ImportExportMixin, UserAdmin):
#     resource_class = UserResource
#     pass


class TasklistAdmin(admin.ModelAdmin):
    search_fields = ['nik','name']
    list_display = ('nik','task','isfinish')
    list_filter = ('date','nik',('date',DateRangeFilter))
    list_per_page = 50


class WorkTimeAdmin(ImportExportModelAdmin):
    search_fields = ['nik','name']
    list_display = ('nik','name','date','time','type_absen','type_work')
    list_filter = (('date',DateRangeFilter),'date','nik',)
    list_per_page = 15



class BdlheaderAdmin(ImportExportModelAdmin):
    search_fields = ['doc_id','emp_no']
    list_display = ('doc_id','emp_no','doc_type','total_payment_idr','approver_1','approver_2','act_state1','act_state2','sts_new')
    list_filter = (('doc_date',DateRangeFilter),'doc_date','emp_no',)
    list_per_page = 15

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(CoordinatUser, CordinatUserAdmin)
admin.site.register(CoordinatOffice,CordinatOfficeAdmin)
admin.site.register(WorkTime,WorkTimeAdmin)
admin.site.register(TimeView, MasterTimeviewAdmin)
admin.site.register(WorkTasklist, TasklistAdmin)
admin.site.register(WorkingcalendarCreate)
admin.site.register(MasterEmployee, MasterEmployeeAdmin)
admin.site.register(Leaveheader, LeaveHeaderAdmin)
admin.site.register(MasterDivision, MasterDivisionAdmin)
admin.site.register(MasterDepartment, MasterDeptAdmin)
admin.site.register(Logbookheader, BdlheaderAdmin)