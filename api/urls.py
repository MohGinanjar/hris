from django.urls import path, re_path
from . import views
from .views import Worktimenik


urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('coordinat-detail/<str:nik>/', views.coordinatdetail, name="coordinat-detail"),
    path('coordinat-detail-wfh-office/<str:nik>/', views.coordinatofficedanwfh, name="coordinat-detail-wfh-office"),
    path('coordinat-update/<str:nik>/', views.coordinatupdate, name="coordinat-update"),
    path('coordinat-update-2/<str:nik>/', views.coordinatupdate2, name="coordinat-update-2"),
    path('coordinat-create/', views.coordinatcreate, name="coordinat-create"),
    path('coordinat-list/', views.coordinatlist, name="coordinat-list"),
    path('work-list/', views.worktimelist, name='work-list'),
    #For WFO
    path('work-clock-in-wfo/', views.worktimeclockinwfo, name='work-clock-in-wfo'),
    path('work-clock-out-wfo/', views.worktimeclockoutwfo, name='work-clock-out-wfo'),
    #For WFH
    path('work-clock-in-wfh/', views.worktimeclockinwfh, name='work-clock-in-wfh'),
    path('work-clock-out-wfh/', views.worktimeclockoutwfh, name='work-clock-out-wfh'),

    # path('work-time-detail/<str:nik>/', views.worktimedetail, name='work-time-detail'),
    re_path('work-time-detail/(?P<nik>.+)/$', Worktimenik.as_view(), name='work-time-detail'),
    path('time-view-user/<str:pin>/', views.timeviewuser, name='time-view-user'),
    path('task-list-user/<str:pin>/<str:date>/', views.tasklistuser, name='task-list-user'),
    path('task-list-user-count/<str:pin>/', views.tasklistusercount, name='task-list-user-count'),
    path('task-list-user-create/', views.tasklistusercreate, name='task-list-user-create'),
    path('task-list-user-create-2/', views.tasklistusercreate2, name='task-list-user-create-2'),
    
    path('task-list-user-update/', views.tasklistuserupdate, name='task-list-user-update'),
    path('task-list-user-delete/', views.tasklistuserdelete, name='task-list-user-delete'),
    path('login-auth/', views.login),

    #For MasterEmployee
    path('master-employee/<str:nik>/', views.masteremployee, name='master-employee'),
    path('user-account/', views.useraccount, name='user-account'),
    #For Leave in out dinas kota
    path('leave-header/', views.leaveheader, name='leave-header'),
    path('leave-header-post/', views.leaveheaderpost, name='leave-header-post'),
    path('leave-header-out/', views.leaveheaderout, name='leave-header-out'),
    path('work-clock-without-wfh/', views.worktimeclockoutwithoutwfh, name='work-clock-without-wfh'),
    path('work-clock-without-wfh-2/', views.worktimeclockoutwithoutwfh2, name='work-clock-without-wfh-2'),
    path('index/', views.indexapi, name='index'),
    path('indexjson/', views.indexapijson, name='indexjson'),
    path('template/', views.cektemplate, name='template'),
    path('detail/<int:pk>/' ,views.detailshowemp,name='detail'),
    path('detail-emp-month/<int:pk>/' ,views.detailshowempmonth,name='detail-emp-month'),
    path('detail-task-list/<int:pk>/' ,views.detailtasklist,name='detail-task-list'),
    path('detail-task-list-month/<int:pk>/' ,views.detailtasklistmonth,name='detail-task-list-month'),
    path('asuransi-reminder/' ,views.sendasuransireminder,name='asuransi-reminder'),
    path('validation-time/' ,views.validationtime,name='validation-time'),
    path('superior-list-member/<str:nik>/' ,views.dropdownlistmembersuperior,name='superior-list-member'),
    path('tasklist-cek-today/<str:nik>/<str:date>/' ,views.cektasklisttoday,name='tasklist-cek-today'),
    path('decrypt/' ,views.decryptdata,name='decrypt'),
    ]