from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CoordinatUserSerializer,WorkTimeSerializer, WorkTimeSerializerlist,TimeViewSerializers,TaskListSerializers,MasterEmployeeSerializers,UseraccountSerializers,CordinatUserSerializer2,LeaveHeaderSerializer,CoordinatUserSerializerUpdate,LeaveHeaderSerializerOut,CoordinatUserSerializerUpdate2,TaskListSerializers2,TaskSerializer,MasterEmployeeSuperiorSerializer,LeaveHeaderSerializerhooh
from .models import CoordinatUser, WorkTime, TimeView, WorkTasklist,MasterEmployee,Useraccount,Leaveheader, MasterDivision
from rest_framework import status,generics
from datetime import datetime, timedelta
import datetime
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from asgiref.sync import sync_to_async
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.utils import timezone
import pytz
from django.core.signing import Signer

signer = Signer()

from django.utils.crypto import pbkdf2
import base64, hashlib

key = "560A18CD0203154CF0A2E8671F9B6B9EA9"

def cektemplate(request):
    return render(request,'charts.html')

def indexapi(request):
    to = datetime.datetime.now().strftime('%Y%m%d')
    tomonth = datetime.datetime.now().strftime('%Y%m')
    wfh = TimeView.objects.filter(type_work='WFH', date=datetime.datetime.now()).count()
    wfo = TimeView.objects.filter(type_work='WFO', date=datetime.datetime.now()).count()
    permit_trip_dalam = Leaveheader.objects.filter(wk_type='P7', from_dt=to).count()
    permit_trip_luar = Leaveheader.objects.filter(wk_type='P3', from_dt=to).count()
    name_wfh = TimeView.objects.filter(type_work='WFH', date=datetime.datetime.now())
    name_wfo = TimeView.objects.filter(type_work='WFO', date=datetime.datetime.now())
    div = MasterEmployee.objects.filter(division_code="124", timeview__type_work='WFH')

    today = datetime.datetime.now()
    division_id = MasterDivision.objects.all().values_list('division_id', flat=True).distinct()
    month_view = datetime.datetime.now().date().strftime('%m')
    group_by_div_today = []
    group_by_div = []
    today_bar = []
    month_bar = []

    for up in division_id:
        division = MasterDivision.objects.filter(division_id=up).first()
        divisi_emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count_wfo = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFO',timeview__date=today).count()
        emp_count_wfh = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today).count()
        emp_count_wfh_isi_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__date=today).values_list('worktasklist__nik').count()
        emp_count_wfh_not_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__isfinish=True,).count()
        not_task =  emp_count_wfh - emp_count_wfh_isi_task
        print(not_task)
        emp_count_permit_dalam = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P3', leaveheader__from_dt=to).count()
        emp_count_permit_luar = MasterEmployee.objects.filter(division_code=up,leaveheader__wk_type='P7', leaveheader__from_dt=to).count()
        today_bar.append(
            {   'division':division,
                'emp_count':emp_count,
                'emp_count_wfo':emp_count_wfo,
                'emp_count_wfh':emp_count_wfh,
                'emp_count_wfh_isi_task':emp_count_wfh_isi_task,
                'emp_count_wfh_not_task':not_task,
                'emp_count_permit_dalam':emp_count_permit_dalam,
                'emp_count_permit_luar':emp_count_permit_luar,
            }
        )

    for up in division_id:
       
        division = MasterDivision.objects.filter(division_id=up).first()
        divisi_emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count_wfo = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFO',timeview__date__month=month_view).count()
        emp_count_wfh = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view).count()
        emp_count_wfh_isi_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view,worktasklist__isfinish=True,).count()
        emp_count_wfh_not_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view,worktasklist__isfinish=False,).count()
        emp_count_permit_dalam = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P3', leaveheader__from_dt__icontains=tomonth).count()
        emp_count_permit_luar = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P7', leaveheader__from_dt__icontains=tomonth).count()
        month_bar.append(
            {   'division':division,
                'emp_count':emp_count,
                'emp_count_wfo':emp_count_wfo,
                'emp_count_wfh':emp_count_wfh,
                'emp_count_wfh_isi_task':emp_count_wfh_isi_task,
                'emp_count_wfh_not_task':emp_count_wfh_not_task,
                'emp_count_permit_dalam':emp_count_permit_dalam,
                'emp_count_permit_luar':emp_count_permit_luar,
            }
        )

    for up in division_id:
        
        division = MasterDivision.objects.filter(division_id=up).first()
        divisi_emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count_wfo = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFO',timeview__date__month=month_view).count()
        emp_count_wfh = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view).count()
        
        emp_count_wfh_isi_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view,worktasklist__date__month=month_view).values_list('worktasklist__nik', flat=True).distinct().count()
        print(emp_count_wfh_isi_task)
        not_task = emp_count_wfh_isi_task - emp_count_wfh
        emp_count_wfh_not_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date__month=month_view,worktasklist__isfinish=False,).count()
        emp_count_permit_dalam = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P3', leaveheader__from_dt__icontains=tomonth).count()
        emp_count_permit_luar = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P7', leaveheader__from_dt__icontains=tomonth).count()
        group_by_div.append(
            {   'division':division,
                'emp_count':emp_count,
                'emp_count_wfo':emp_count_wfo,
                'emp_count_wfh':emp_count_wfh,
                'emp_count_wfh_isi_task':emp_count_wfh_isi_task,
                'emp_count_wfh_not_task':not_task,
                'emp_count_permit_dalam':emp_count_permit_dalam,
                'emp_count_permit_luar':emp_count_permit_luar,
            }
        )
     
    for up in division_id:
        division = MasterDivision.objects.filter(division_id=up).first()
        divisi_emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count_wfo = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFO',timeview__date=today).count()
        emp_count_wfh = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today).count()
        emp_count_wfh_isi_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__date=today).values_list('worktasklist__nik', flat=True).distinct().count()
        emp_count_wfh_not_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__isfinish=False,).count()
        not_task = emp_count_wfh_isi_task - emp_count_wfh
        emp_count_permit_dalam = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P3', leaveheader__from_dt=to).count()
        emp_count_permit_luar = MasterEmployee.objects.filter(division_code=up,leaveheader__wk_type='P7', leaveheader__from_dt=to).count()
        group_by_div_today.append(
            {   'division':division,
                'emp_count':emp_count,
                'emp_count_wfo':emp_count_wfo,
                'emp_count_wfh':emp_count_wfh,
                'emp_count_wfh_isi_task':emp_count_wfh_isi_task,
                'emp_count_wfh_not_task':not_task,
                'emp_count_permit_dalam':emp_count_permit_dalam,
                'emp_count_permit_luar':emp_count_permit_luar,
            }
        )

    # paginator = Paginator(group_by_div_today, 10)
    # page_number = request.GET.get('page',1)
    # page_obj = paginator.get_page(page_number)

    page = request.GET.get('page', 1)

    paginator = Paginator(group_by_div_today, 7)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    

    pages = request.GET.get('pages', 1)

    paginator = Paginator(group_by_div, 7)
    try:
        groupdiv = paginator.page(pages)
    except PageNotAnInteger:
        groupdiv = paginator.page(1)
    except EmptyPage:
        groupdiv = paginator.page(paginator.num_pages)

    context = {
        'month_bar':month_bar,
        'today_bar':today_bar,
        'group_by_div':groupdiv,
        'division_id':division_id,
        'group_by_div_today':users,
        # 'total_emp':total_emp,
        'today':today,
        'wfh':wfh,
        'wfo':wfo,
        'permit_trip_luar':permit_trip_luar,
        'permit_trip_dalam':permit_trip_dalam,
        'name_wfh':name_wfh,
        'name_wfo':name_wfo,
        
        
    }
    return render(request,"snippets/layout/index.html", context)

    get_blog = sync_to_async(indexapi, thread_sensitive=True)


def detailshowemp(request, pk):
    today = datetime.datetime.now().strftime('%d')
    instance = MasterEmployee.objects.filter(division_code=pk, status_emp='active', timeview__date__day=today,)
    context = {
        'instance': instance
    }
    return render(request, 'detail.html', context)

def detailshowempmonth(request, pk):
    today = datetime.datetime.now().strftime('%m')
    instance = MasterEmployee.objects.filter(division_code=pk, status_emp='active', timeview__date__month=today,)
    context = {
        'instance': instance,
    }
    return render(request, 'detail_emp_month.html', context)


def detailtasklist(request, pk):
    today = datetime.datetime.now().strftime('%d')
    instance = WorkTasklist.objects.filter(nik=pk, date__day=today)
    print(instance)
    context = {
        'instance': instance
    }
    return render(request, 'detail_task_list.html', context)

def detailtasklistmonth(request, pk):
    today = datetime.datetime.now().strftime('%m')
    instance = WorkTasklist.objects.filter(nik=pk, date__day=today,)
    print(instance)
    context = {
        'instance': instance
    }
    return render(request, 'detail_task_list_month.html', context)



def indexapijson(request):
    to = datetime.datetime.now().strftime('%Y%m%d')
    tomonth = datetime.datetime.now().strftime('%Y%m')
    today = datetime.datetime.now()
    division_id = MasterDivision.objects.all().values_list('division_id', flat=True).distinct()
    month_view = datetime.datetime.now().date().strftime('%m')
    group_by_div_today = []
    for up in division_id:
        division = MasterDivision.objects.filter(division_id=up).first()
        divisi_emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count = MasterEmployee.objects.filter(division_code=up, status_emp='active').count()
        emp_count_wfo = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFO',timeview__date=today).count()
        emp_count_wfh = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today).count()
        emp_count_wfh_isi_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__date=today).values_list('worktasklist__nik').count()
        emp_count_wfh_not_task = MasterEmployee.objects.filter(division_code=up, status_emp='active',timeview__type_work='WFH',timeview__date=today,worktasklist__isfinish=False,).count()
        emp_count_permit_dalam = MasterEmployee.objects.filter(division_code=up, status_emp='active',leaveheader__wk_type='P3', leaveheader__from_dt=to).count()
        emp_count_permit_luar = MasterEmployee.objects.filter(division_code=up,leaveheader__wk_type='P7', leaveheader__from_dt=to).count()
        group_by_div_today.append(
            {   'division':division.division_name,
                'emp_count':emp_count,
                'emp_count_wfo':emp_count_wfo,
                'emp_count_wfh':emp_count_wfh,
                'emp_count_wfh_isi_task':emp_count_wfh_isi_task,
                'emp_count_wfh_not_task':emp_count_wfh_not_task,
                'emp_count_permit_dalam':emp_count_permit_dalam,
                'emp_count_permit_luar':emp_count_permit_luar,
            }
        )
    return JsonResponse(group_by_div_today, safe=False)

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/coordinat-list/',
        'Detail':'/coordinat-detail/<str:pk>',
        'Create':'/coordinate-create/',
        'Update': '/coordinate-update',
        'Delete':'/coordinate-delete',
        'Work':'/work-list/',
    }
    return Response(api_urls)

####GET TOKEN FOR ACCSESS URL####

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

### "token": "790003f78e5776bf36305d267f59758441a4795d"

#### MODUL COORDINAT USER ####

@api_view(['GET'])
def coordinatlist(request):
    coordinat = CoordinatUser.objects.all()
    serializer = CoordinatUserSerializer(coordinat, many=True)
    return Response ({"data" : serializer.data})



@api_view(['GET'])
def coordinatdetail(request, nik):
    coordinat = CoordinatUser.objects.get(nik=nik)
    serializer = CoordinatUserSerializer(coordinat, many=False)
    return Response({"data" : serializer.data})

@api_view(['GET'])
def coordinatofficedanwfh(request, nik):
    coordinat = CoordinatUser.objects.get(nik=nik)
    serializer = CordinatUserSerializer2(coordinat, many=False)
    return Response({"data" : serializer.data})

# @api_view(['POST'])
# def coordinatcreate(request):
#     serializer = CoordinatUserSerializer(data=request.data)
#     if CoordinatUser.objects.filter(nik=request.data['nik']).exists():
#         return Response({"error": "This data id already exists." ,"value":2})
#     if serializer.is_valid():
#         serializer.save()
#         content = {"message":"Sukses Masuk", "value":1}
#         return JsonResponse(content, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def coordinatcreate(request):
    serializer = CoordinatUserSerializer(data=request.data)
    userloc = MasterEmployee.objects.get(emp_no=request.data['nik'])
    location = userloc.location_code
    if location == 'MTH':
        location = 1
    elif location == 'JTK':
        location = 2
    elif location == 'KBI':
        location = 4
    elif location == 'MDN':
        location = 5
    elif location == 'SBY':
        location = 6
    else :
        location = 1
    print(location)
    if CoordinatUser.objects.filter(nik=request.data['nik']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.validated_data['office1_id']= location
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# server = 'tms7'
# database = 'tms7' 
# username = 'dba'
# password = 'soy'
# # <====== Adaptive Server Anywhere 7.0, not support
# 'DRIVER={SQL Server};SERVER=192.168.123.456;PORT=1433;DATABASE=yourdb;UID=your_user;PWD=your_pw;'


# server = 'tms7'
# port ='1433' 
# database = 'tms7' 
# username = 'DBA' 
# password = 'SOY'


# cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

# cnxn = pyodbc.connect(
#     'DRIVER={SQL Server};'
#     'Server=tms7'
#     'PORT=1433'
#     'DATABASE=tms7' 
#     'uid=dba' 
#     'pwd=soy')
# cursor = cnxn.cursor()


@api_view(['POST'])
def coordinatupdate(request, nik):
    if CoordinatUser.objects.filter(nik=request.data['nik'], name=request.data['name']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    cord = CoordinatUser.objects.get(nik=nik)
    serializer = CoordinatUserSerializerUpdate(instance=cord, data=request.data)
    if serializer.is_valid():
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.data)


@api_view(['POST'])
def coordinatupdate2(request, nik):
    if CoordinatUser.objects.filter(nik=request.data['nik'], lat__isnull=True,long__isnull=True).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if CoordinatUser.objects.filter(nik=request.data['nik'], lat2__isnull=False,long2__isnull=False).exists():
        return Response({"error": "This data id already exists." ,"value":3})
    cord = CoordinatUser.objects.get(nik=nik)
    serializer = CoordinatUserSerializerUpdate2(instance=cord, data=request.data)
    if serializer.is_valid():
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.data)



@api_view(['POST'])
def coordinatdelete(request, nik):
    cord = CoordinatUser.objects.get(nik=nik)
    cord.delete()
    return Response("delete sukses !!")


##MODUL WORK TIME USER###

@api_view(['GET'])
def worktimelist(request):
    worktime = WorkTime.objects.all()
    serializer = WorkTimeSerializer(worktime, many=True)
    return Response ({"data" : serializer.data})

# @csrf_exempt
# @api_view(['GET'])
# def worktimedetail(request, nik):
#     worktime = WorkTime.objects.filter(nik=nik)
#     serializer = WorkTimeSerializer(worktime, many=False)
#     return Response ({"data" : serializer.data})

class Worktimenik(generics.ListAPIView):
    serializer_class = WorkTimeSerializerlist
    def get_queryset(self):
        nik = self.kwargs['nik']
        return WorkTime.objects.filter(nik__iexact=nik)

from django.contrib.auth.hashers import make_password
    
@csrf_exempt
@api_view(['POST'])
def worktimeclockinwfo(request):
    nik_to = request.data['nik']
    nik = request.data['nik']
    date = request.data['date']
    type_absen= request.data['type_absen']
    time_in_data = request.data['time']
    type_works = request.data['type_work']
    # email = Useraccount.objects.filter(emp_no=nik).values_list('mail_acc', flat=True).distinct()
    # encrypt = make_password("36721")
    # print(encrypt)
    # testnik = "Um50S0d1UW5WN1NmWGJwbkY3V3UrUT09"
    # result = hashlib.sha256(nik.encode('ascii')).hexdigest()
    # print(result)
    # dateconvert = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%Y%m%d')
    # print(dateconvert)
    # subject = "Notification Desk Work WFO"
    # email_from = settings.EMAIL_HOST_USER
    # to = email
    # text_content = 'This is an important message.'
    # html_message =  loader.render_to_string(
    #         'message_wfo_clock_in.html',
    #         {   
    #             'nik':nik,
    #             'date':"210",
    #             'encrypt':result
                
    #         }
    #     )
    # send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFH').exists():
        return Response({"error": "Anda tadi melakukan absen WFH" ,"value":4})
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        TimeView.objects.get_or_create(nik=nik,name=request.data['name'].title(), date=date, time_in=time_in_data, type_work=type_works, data_emp_id=nik_to)
        serializer.save()
        ## send - > get paramater email from masteremployee to self employee
        # send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def worktimeclockoutwfo(request):
    serializer = WorkTimeSerializer(data=request.data)
    nik_to = request.data['nik']
    nik = request.data['nik']
    date = request.data['date']
    type_absen= request.data['type_absen']
    time_out_data = request.data['time']
    type_works = request.data['type_work']
    duration_work = request.data['duration_work']
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFH').exists():
        return Response({"error": "Anda tadi melakukan absen WFH" ,"value":4})
    cek_data = WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work=request.data['type_work']).exists()
    if cek_data == False:
        return Response({"error": "Belum Clock IN" ,"value":3})
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        TimeView.objects.filter(nik=nik, date=date).update(time_out=time_out_data,type_work=type_works, duration_work=duration_work) 
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def worktimeclockinwfh(request):
    nik_to = request.data['nik']
    nik = request.data['nik']
    date = request.data['date']
    type_absen= request.data['type_absen']
    type_work=request.data['type_work']
    time_in_data = request.data['time']
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFO').exists():
        return Response({"error": "Anda tadi melakukan absen WFH/WFO" ,"value":4})
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        TimeView.objects.get_or_create(nik=nik,name=request.data['name'].title(), date=date, time_in=time_in_data, type_work=type_work, data_emp_id=nik_to)
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def worktimeclockoutwfh(request):
    nik_to = request.data['nik']
    nik = request.data['nik']
    date = request.data['date']
    type_absen= request.data['type_absen']
    time_out_data = request.data['time']
    type_works = request.data['type_work']
    duration_work = request.data['duration_work']
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], status_absen='Adjust', type_work='WFO').exists():
        return Response({"error": "This data id already exists." ,"value":5})
    cek_status = WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFO').exists()
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFO').exists():
        return Response({"error": "Anda tadi melakukan absen WFH/WFO" ,"value":4})
    cek_data = WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work=request.data['type_work']).exists()
    if cek_data == False:
        return Response({"error": "Belum Clock IN" ,"value":3})
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        TimeView.objects.filter(nik=nik, date=date).update(time_out=time_out_data,type_work=type_works, duration_work=duration_work) 
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def worktimeclockoutwithoutwfh(request):
    nik = request.data['nik']
    reason = request.data['reason']
    date = request.data['date']
    type_absen= request.data['type_absen']
    time_out_data = request.data['time']
    type_works = request.data['type_work']
    duration_work = request.data['duration_work']
    ref_id = request.data['ref_id']
    email = request.data['email1']
    name_approved1 = request.data['namesuperior1'].title()
    emp_no = request.data['emp_no']
    emp_name = request.data['emp_name'].title()
    out_time = request.data['out_time']
    from_dt = request.data['from_dt']
    print(from_dt)
    date = datetime.datetime.strptime(from_dt, '%y%m%d').strftime('%Y-%m-%d')
    print("ini date bener" + date)
    wk_type = request.data['wk_type']
    if wk_type == "HO":
        wk_type = "Working From Home To Office"
    elif wk_type == "P7":
        wk_type = "Perjalanan Dinas Luar Kota"
    elif wk_type == "AFH":
        wk_type = "Work Form Another Location"
    elif wk_type == "OH":
        wk_type = "Working Forget Clock out in Office"
    # email2 = request.data['email2']
    subject = "Notification Request Leave by HRIS Apss"
    email_from = settings.EMAIL_HOST_USER
    to = [email,]
    text_content = 'This is an important message.'
    in_time_in = Leaveheader.objects.filter(ref_id=ref_id)
    html_message =  loader.render_to_string(
            'message_wfh.html',
            {   
                'approved':name_approved1,
                'user_name': emp_name,
                'subject':  subject,
                'ref_id':ref_id,
                'emp_no':emp_no,
                'emp_name':emp_name,
                'reason': reason,
                'out_time':out_time,
                'ijin':wk_type,
                'date':date,
                'in_time_after':in_time_in,
                
            }
        )
    serializerleave = LeaveHeaderSerializer(data=request.data)
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik']
     ,date=request.data['date'],
      type_absen=request.data['type_absen'],
      status_absen=request.data['status_absen'], 
      type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid() and serializerleave.is_valid():
        TimeView.objects.filter(nik=request.data['nik'], date=request.data['date']).update(time_out=time_out_data,type_work=type_works, duration_work=duration_work)
        serializer.save()
        send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)
        serializerleave.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def worktimeclockoutwithoutwfh2(request):
    reason = request.data['reason']
    date = request.data['date']
    time_out_data = request.data['time']
    type_works = request.data['type_work']
    duration_work = request.data['duration_work']
    ref_id = request.data['ref_id']
    email = request.data['email1']
    name_approved1 = request.data['namesuperior1'].title()
    emp_no = request.data['emp_no']
    emp_name = request.data['emp_name'].title()
    out_time = request.data['out_time']
    wk_type = request.data['wk_type']
    if wk_type == "HO":
        wk_type = "Working From Home To Office"
    elif wk_type == "P7":
        wk_type = "Perjalanan Dinas Luar Kota"
    elif wk_type == "AFH":
        wk_type = "Work Form Another Location"
    elif wk_type == "OH":
        wk_type = "Working Forget Clock out in Office"
    # email2 = request.data['email2']
    subject = "Notification Request Leave by HRIS Apss"
    email_from = settings.EMAIL_HOST_USER
    to = [email,]
    text_content = 'This is an important message.'
    in_time_in = Leaveheader.objects.filter(ref_id=ref_id)
    html_message =  loader.render_to_string(
            'message_wfh.html',
            {   
                'approved':name_approved1,
                'user_name': emp_name,
                'subject':  subject,
                'ref_id':ref_id,
                'emp_no':emp_no,
                'emp_name':emp_name,
                'reason': reason,
                'out_time':out_time,
                'ijin':wk_type,
                'date':date,
                'in_time_after':in_time_in,
                
            }
        )
    
    serializerleave = LeaveHeaderSerializerhooh(data=request.data)
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik']
     ,date=request.data['date'],
      type_absen=request.data['type_absen'],
      status_absen=request.data['status_absen'], 
      type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid() and serializerleave.is_valid():
        TimeView.objects.filter(nik=request.data['nik'], date=request.data['date']).update(time_out=time_out_data,type_work=type_works, duration_work=duration_work)
        serializer.save()
        send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)
        serializerleave.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# date__month=month_view

@api_view(['GET'])
def timeviewuser(request, pin):
    month_view = datetime.datetime.now().date().strftime('%m')
    snippets = TimeView.objects.filter(nik=pin,)
    serializer = TimeViewSerializers(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tasklistuser(request, pin, date):
    month_view = datetime.datetime.now().date().strftime('%m')
    snippets = WorkTasklist.objects.filter(nik=pin, date=date)
    serializer = TaskListSerializers(snippets, many=True)
    return Response(serializer.data)


# get count task list user

@api_view(['GET'])
def tasklistusercount(request, pin):
    snippets = WorkTasklist.objects.filter(nik=pin)
    serializer = TaskSerializer(snippets, many=True)
    return Response({"data" : serializer.data})




@api_view(['GET'])
def tasklistuser(request, pin, date):
    month_view = datetime.datetime.now().date().strftime('%m')
    snippets = WorkTasklist.objects.filter(nik=pin, date=date)
    serializer = TaskListSerializers(snippets, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def tasklistusercreate(request):
    nik_to = request.data['nik']
    serializer = TaskListSerializers(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def tasklistuserdelete(request):
    id = request.data['id']
    cord = WorkTasklist.objects.get(id=id)
    cord.delete()
    return Response({"value":"delete sukses !!"})


@api_view(['POST'])
def tasklistusercreate2(request):
    nik_to = request.data['nik']
    serializer = TaskListSerializers2(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(['POST'])
def tasklistuserupdate(request):
    id = request.data['id']
    cord = WorkTasklist.objects.get(id=id)
    serializer = TaskListSerializers(instance=cord, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def cektasklisttoday(request, nik, date):
    tasklistcount =  WorkTasklist.objects.filter(nik=nik, date=date, isfinish=1).count()
    print(tasklistcount)
    if tasklistcount == 3 or tasklistcount >= 3:
        return Response({"message": "Ada Task List" ,"value":1})
    else :
        return Response({"message": "Anda belum membuat Task List hari ini silahkan untuk membuat Task list minimal 3 Task List agar bisa melakukan clock out" ,"value":2})




@api_view(['GET'])
def masteremployee(request,nik):
    snippets = MasterEmployee.objects.filter(emp_no=nik)
    serializer = MasterEmployeeSerializers(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def useraccount(request):
    snippets = Useraccount.objects.all()
    serializer = UseraccountSerializers(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def leaveheader(request):
    snippets = Leaveheader.objects.all()
    serializer = LeaveHeaderSerializer(snippets, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def leaveheaderout(request):
    ref_id = request.data['ref_id']
    email = request.data['email1']
    name_approved1 = request.data['namesuperior1'].title()
    emp_no = request.data['emp_no']
    emp_name = request.data['emp_name'].title()
    # reason = request.data['reason']
    out_time = request.data['out_time']
    # destination = request.data['destination']
    from_dt = request.data['finish_dt']
    date = datetime.datetime.strptime(from_dt, '%Y%m%d').strftime('%Y-%m-%d')
    print(date)
    wk_type = request.data['wk_type']
    if wk_type == "P3":
        wk_type = "Perjalanan Dinas Dalam Kota"
    elif wk_type == "P7":
        wk_type = "Perjalanan Dinas Luar Kota"
    elif wk_type == "AFH":
        wk_type = "Work Form Another Home Location"
    # email2 = request.data['email2']
    subject = "Notification Request Leave by HRIS Apss"
    email_from = settings.EMAIL_HOST_USER
    to = [email,]
    text_content = 'This is an important message.'
    in_time_in = Leaveheader.objects.filter(ref_id=ref_id)
    html_message =  loader.render_to_string(
            'message.html',
            {   
                'approved':name_approved1,
                'user_name': emp_name,
                'subject':  subject,
                'ref_id':ref_id,
                'emp_no':emp_no,
                'emp_name':emp_name,
                'out_time':out_time,
                'ijin':wk_type,
                'date':date,
                'in_time_after':in_time_in
                
            }
        )
    if Leaveheader.objects.filter(ref_id=ref_id, emp_no=emp_no, finish_dt=from_dt).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    cord = Leaveheader.objects.get(ref_id=ref_id)
    print(cord)
    serializer = LeaveHeaderSerializerOut(instance=cord, data=request.data)
    if serializer.is_valid():
        TimeView.objects.filter(nik=emp_no, date=date).update(time_out=out_time)
        serializer.save()
        send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def leaveheaderpost(request):
    nik_to = request.data['emp_no']
    from_dt = request.data['from_dt']
    date = datetime.datetime.strptime(from_dt, '%Y%m%d').strftime('%Y-%m-%d')
    time_in = request.data['in_time']
    wk_type = request.data['wk_type']

    if wk_type == 'P7':
        wk_type = 'WFT'
    elif wk_type == 'P3':
        wk_type = 'WFT'

    serializer = LeaveHeaderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['data_emp_id']= nik_to
        TimeView.objects.get_or_create(nik=nik_to,name=request.data['emp_name'].title(), date=date, time_in=time_in, type_work=wk_type, data_emp_id=nik_to)
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ####### this action to get time in trip ############
    # ref_id = request.data['ref_id']
    # email = request.data['email1']
    # name_approved1 = request.data['namesuperior1'].title()
    # emp_no = request.data['emp_no']
    # emp_name = request.data['emp_name'].title()
    # reason = request.data['reason']
    # in_time = request.data['in_time']
    # destination = request.data['destination']
    # from_dt = request.data['from_dt']
    # date = datetime.datetime.strptime(from_dt, '%Y%m%d').strftime('%Y-%m-%d')
    # print(date)
    # wk_type = request.data['wk_type']
    # if wk_type == "P3":
    #     wk_type = "Perjalanan Dinas Dalam Kota"
    # elif wk_type == "P7":
    #     wk_type = "Perjalanan Dinas Luar Kota"
    # # email2 = request.data['email2']
    # subject = "Notification Request Leave by HRIS Apss"
    # email_from = settings.EMAIL_HOST_USER
    # to = [email]
    # text_content = 'This is an important message.'
    
    # html_message =  loader.render_to_string(
    #         'message.html',
    #         {   
    #             'approved':name_approved1,
    #             'user_name': "Mohamad Ginanjar",
    #             'subject':  subject,
    #             'ref_id':ref_id,
    #             'emp_no':emp_no,
    #             'emp_name':emp_name,
    #             'reason': reason,
    #             'in_time':in_time,
    #             'destination':destination,
    #             'ijin':wk_type,
    #             'date':date,
                
    #         }
    #     )
    # send_mail(subject, text_content, email_from, to, fail_silently=True, html_message=html_message)


    

# @api_view(['POST'])
# def worktimeclockoutwfh(request):
#     serializer = WorkTimeSerializer(data=request.data)
#     nik = request.data['nik']
#     date = request.data['date']
#     type_absen= request.data['type_absen']
#     time_out_data = request.data['time']
#     if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work='WFO').exists():
#         return Response({"error": "Anda tadi melakukan absen WFO" ,"value":4})
#     cek_data = WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen='CLOCK_IN', type_work=request.data['type_work']).exists()
#     if cek_data == False:
#         return Response({"error": "Belum Clock IN" ,"value":3})
#     if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
#         return Response({"error": "This data id already exists." ,"value":2}
#     TimeView.objects.filter(nik=nik, date=date).update(time_out=time_out_data)
#     if serializer.is_valid():
#         serializer.save()
#         content = {"message":"Sukses Masuk", "value":1}
#         return JsonResponse(content, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def worktimeclockout(request):
    serializer = WorkTimeSerializer(data=request.data)
    if WorkTime.objects.filter(nik=request.data['nik'] ,date=request.data['date'], type_absen=request.data['type_absen'], type_work=request.data['type_work']).exists():
        return Response({"error": "This data id already exists." ,"value":2})
    if serializer.is_valid():
        serializer.save()
        content = {"message":"Sukses Masuk", "value":1}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class CoordinatCreate(generics.CreateAPIView):
#     queryset = CoordinatUser.objects.all()
#     serializer_class = CoordinatUserSerializer


# class CoordinatList(generics.ListAPIView):
#     queryset = CoordinatUser.objects.all()
#     serializer_class = CoordinatUserSerializer
#     # def get(self, request):
#     #     queryset = CoordinatUser.objects.all()
#     #     serializer = CoordinatUserSerializer(queryset, many=True)
#     #     return Response(serializer.data)

# class CoordinatUpdate(generics.RetrieveUpdateAPIView):
#     queryset = CoordinatUser.objects.all()
#     serializer_class = CoordinatUserSerializer

# class CoordinatDelete(generics.DestroyAPIView):
#     queryset = CoordinatUser.objects.all()
#     serializer_class = CoordinatUserSerializer



def sendasuransireminder(request):
    return HttpResponse('Done!')




def validationtime(request):
    zone = timezone.localtime(timezone.now())
    timezo = zone.strftime("%Y-%m-%d %H:%M:%S")
    time = datetime.datetime.now()
    now = time.strftime("%Y-%m-%d %H:%M")
    date = zone.strftime("%Y-%m-%d %H:%M")

    # set zone in country Indonesia
    jkt = pytz.timezone("Asia/jakarta")
    mks = pytz.timezone("Asia/Makassar")
    jypr = pytz.timezone("Asia/Jayapura")
    ptnk = pytz.timezone("Asia/Pontianak")

    # set curent time 
    dt_jkt = datetime.datetime.now(jkt)
    dt_mks = datetime.datetime.now(mks)
    dt_jypr = datetime.datetime.now(jypr)
    dt_ptnk = datetime.datetime.now(ptnk)

    # set time convert
    jakartatime = dt_jkt.strftime("%Y-%m-%d %H:%M")
    makassartime = dt_mks.strftime("%Y-%m-%d %H:%M")
    jayapuratime = dt_jypr.strftime("%Y-%m-%d %H:%M")
    pontianaktime = dt_jypr.strftime("%Y-%m-%d %H:%M")
    content = {"time": date, "zone":now, "WIB":jakartatime, "WIT":makassartime, "WITA":jayapuratime, "Pontianak":pontianaktime}
    return JsonResponse(content)

@api_view(['GET'])
def dropdownlistmembersuperior(request, nik):
    snippets = MasterEmployee.objects.filter(approverid1=nik)
    serializer = MasterEmployeeSuperiorSerializer(snippets, many=True)
    return Response(serializer.data)

# from .crypt import decrypt

def decryptdata(request):
    nik = "2kk39jhi5OrCLqlaIfJRMA=="
    key = "560A18CD0203154CF0A2E8671F9B6B9EA9"
    # result = decrypt(nik, key)
    content ={"hello": key}
    return JsonResponse(content)