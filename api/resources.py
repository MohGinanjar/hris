from import_export import resources
from .models import *


class WorkingCalenderResource(resources.ModelResource):
    class Meta:
        model   = Workingcalendar
        fields = ("wk_day","wk_type","wk_desc","arriv_time","out_time","group_id","dy_name","yyyy","crt_dt","user_id")
    


class InsuranceResource(resources.ModelResource):
    class Meta:
        model   = InsurResult
        fields = ("comment","emp_no","result_insur")
        exclude = ('id',)
        import_id_fields = ['id',]
    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None