from rest_framework import serializers
from .models import CoordinatUser, WorkTime, TimeView, WorkTasklist,MasterEmployee,Useraccount,Leaveheader
from rest_framework.response import Response


class CoordinatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatUser
        fields = ('nik','name','lat', 'long', 'address', 'office1', 'office2', 'office3', 'office4','office5','office6')

    def to_representation(self, instance):
        rep = super(CoordinatUserSerializer, self).to_representation(instance)
        rep['office1'] = {"latoffice": instance.office1.latoffice,"longoffice": instance.office1.longoffice}
        rep['office2'] = {"latoffice": instance.office2.latoffice,"longoffice": instance.office2.longoffice}
        rep['office3'] = {"latoffice": instance.office3.latoffice,"longoffice": instance.office3.longoffice}
        rep['office4'] = {"latoffice": instance.office4.latoffice,"longoffice": instance.office4.longoffice}
        rep['office5'] = {"latoffice": instance.office5.latoffice,"longoffice": instance.office5.longoffice}
        rep['office6'] = {"latoffice": instance.office6.latoffice,"longoffice": instance.office6.longoffice}
        return rep


class CoordinatUserSerializerUpdate2(serializers.ModelSerializer):
    class Meta:
        model = CoordinatUser
        fields = ('nik','lat2','long2')


class CoordinatUserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = CoordinatUser
        fields = ('nik','name','lat', 'long', 'address')



class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ('nik', 'name','date', 'time', 'lat', 'long', 'type_absen',
                  'alamat', 'status_absen', 'type_work', 'duration_work')


class WorkTimeSerializerlist(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ['nik','name', 'date', 'time', 'lat', 'long', 'type_absen',
                  'alamat', 'status_absen', 'type_work', 'duration_work']


class TimeViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = TimeView
        fields = ['nik','name', 'date', 'time_in',
                  'time_out', 'type_work', 'duration_work']


class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkTasklist
        fields = ['id','nik','name', 'task', 'isfinish', 'create_task', 'date']


class TaskListSerializers2(serializers.ModelSerializer):
    class Meta:
        model = WorkTasklist
        fields = ['id','nik','name', 'task', 'isfinish', 'date']


    
   
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTasklist
        fields = ('nik','date')


class UseraccountSerializers(serializers.ModelSerializer):
    name_approved1 = serializers.SerializerMethodField('get_name_approved1')

    def get_name_approved1(self, employee):
        emp_name = MasterEmployee.objects.filter(emp_no=employee.user_acc)
        print(emp_name)
        serializer = GetNameEmployeeSerializer(instance=emp_name, many=True)
        return serializer.data
    
    class Meta:
        model = Useraccount
        fields = ('user_acc','mail_acc','name_approved1')


class GetNameEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterEmployee
        fields = ('emp_name',)


class MasterEmployeeSerializers(serializers.ModelSerializer):
    email_approved1 = serializers.SerializerMethodField('get_email1')
    email_approved2 = serializers.SerializerMethodField('get_email2')
    coordinat = serializers.SerializerMethodField('get_coordinat')
    

    def get_coordinat(self, coordinat_user):
        coordinats = CoordinatUser.objects.filter(nik=coordinat_user.emp_no)
        serializer = CordinatUserSerializer2(instance=coordinats,many=True)
        return serializer.data

    def get_email1(self, useraccount):
        email_1 = Useraccount.objects.filter(user_acc=useraccount.approverid1,)
        serializer = UseraccountSerializers(instance=email_1, many=True)
        return serializer.data

    def get_email2(self, useraccount):
        email_2 = Useraccount.objects.filter(user_acc=useraccount.approverid2,)
        serializer = UseraccountSerializers(instance=email_2, many=True)
        return serializer.data
    class Meta:
        model = MasterEmployee
        fields = ('emp_no','emp_name','approverid1','approverid2','email_approved1','email_approved2','coordinat',)


class CordinatUserSerializer2(serializers.ModelSerializer):
    tracks = MasterEmployeeSerializers(many=True, read_only=True)
    class Meta:
        model = CoordinatUser
        fields =['nik', 'lat', 'long','lat2','long2','radius2','radius','office1','office2','office3','office4','office5','office6', 'address','tracks']

    def to_representation(self, instance):
        rep = super(CordinatUserSerializer2, self).to_representation(instance)
        if rep['office1'] is None:
            rep['office1'] = {"latoffice": None,"longoffice": None, "radius":None, "timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office1'] = {"latoffice": instance.office1.latoffice, "longoffice": instance.office1.longoffice, "radius":instance.office1.radius,"timereminder1":instance.office1.reminder_time1,"timereminder2":instance.office1.reminder_time2, "location":instance.office1.title}

        if rep['office2'] is None:
            rep['office2'] = {"latoffice": None,"longoffice": None, "radius":None,"timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office2'] = {"latoffice": instance.office2.latoffice, "longoffice": instance.office2.longoffice, "radius":instance.office2.radius,"timereminder1":instance.office2.reminder_time1,"timereminder2":instance.office2.reminder_time2,"location":instance.office2.title}
        if rep['office3'] is None:
            rep['office3'] = {"latoffice": None,"longoffice": None, "radius":None,"timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office3'] = {"latoffice": instance.office3.latoffice, "longoffice": instance.office3.longoffice, "radius":instance.office3.radius,"timereminder1":instance.office3.reminder_time1,"timereminder2":instance.office3.reminder_time2, "location":instance.office3.title}
        if rep['office4'] is None:
            rep['office4'] = {"latoffice": None,"longoffice": None, "radius":None,"timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office4'] = {"latoffice": instance.office4.latoffice, "longoffice": instance.office4.longoffice, "radius":instance.office4.radius,"timereminder1":instance.office4.reminder_time1,"timereminder2":instance.office4.reminder_time2, "location":instance.office4.title}
        if rep['office5'] is None:
            rep['office5'] = {"latoffice": None,"longoffice": None, "radius":None, "timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office5'] = {"latoffice": instance.office5.latoffice, "longoffice": instance.office5.longoffice, "radius":instance.office5.radius,"timereminder1":instance.office5.reminder_time1,"timereminder2":instance.office5.reminder_time2,"location":instance.office5.title}
        if rep['office6'] is None:
            rep['office6'] = {"latoffice": None,"longoffice": None, "radius":None, "timereminder1":None, "timereminder2":None, "location":None}
        else:
            rep['office6'] = {"latoffice": instance.office6.latoffice, "longoffice": instance.office6.longoffice, "radius":instance.office6.radius,"timereminder1":instance.office6.reminder_time1,"timereminder2":instance.office6.reminder_time2, "location":instance.office6.title}
        return rep

class LeaveHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaveheader
        fields = ['ref_id','annual_period','emp_no','user_id','wk_type','from_dt','approver_1','approver_2','destination','reason','act_key','del_key','status', 'act_state1','act_state2','act_state3','in_time','out_time']

class LeaveHeaderSerializerhooh(serializers.ModelSerializer):
    class Meta:
        model = Leaveheader
        fields = ['ref_id','annual_period','emp_no','user_id','wk_type','from_dt','finish_dt','approver_1','approver_2','destination','reason','act_key','del_key','status', 'act_state1','act_state2','act_state3','in_time','out_time']


class LeaveHeaderSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Leaveheader
        fields = ['ref_id','annual_period','emp_no','user_id','wk_type','finish_dt','approver_1','approver_2','act_key','del_key','status', 'act_state1','act_state2','act_state3','in_time','out_time']



class MasterEmployeeSuperiorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterEmployee
        fields = ('emp_no','emp_name','approverid1','approverid2')