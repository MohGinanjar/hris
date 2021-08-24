# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activeperiod(models.Model):
    period = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activeperiod'


class ApiCoordinatoffice(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    latoffice = models.FloatField(blank=True, null=True)
    longoffice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_coordinatoffice'


class ApiCoordinatuser(models.Model):
    nik = models.CharField(max_length=6)
    lat = models.FloatField()
    long = models.FloatField()
    address = models.CharField(max_length=100)
    time = models.DateTimeField()
    office1 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)
    office2 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)
    office3 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)
    office4 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)
    office5 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)
    office6 = models.ForeignKey(ApiCoordinatoffice, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_coordinatuser'


class ApiTimeview(models.Model):
    nik = models.CharField(max_length=6)
    date = models.DateField()
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    type_work = models.CharField(max_length=4, blank=True, null=True)
    duration_work = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_timeview'


class ApiWorktasklist(models.Model):
    nik = models.CharField(max_length=6)
    task = models.TextField()
    isfinish = models.IntegerField()
    create_task = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'api_worktasklist'


class ApiWorktime(models.Model):
    nik = models.CharField(max_length=6)
    date = models.DateField()
    time = models.TimeField()
    lat = models.FloatField()
    long = models.FloatField()
    type_absen = models.CharField(max_length=10)
    alamat = models.CharField(max_length=100)
    status_absen = models.CharField(max_length=12)
    type_work = models.CharField(max_length=4)
    duration_work = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_worktime'


class Audittrail(models.Model):
    datetime = models.DateTimeField()
    script = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    table = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    keyvalue = models.TextField(blank=True, null=True)
    oldvalue = models.TextField(blank=True, null=True)
    newvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audittrail'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Company(models.Model):
    company_id = models.CharField(unique=True, max_length=25)
    company_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    company_id = models.CharField(max_length=25)
    employee_id = models.BigIntegerField(blank=True, null=True)
    employee_phone = models.CharField(max_length=30)
    employee_simcard = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeForUpdate(models.Model):
    company_id = models.CharField(max_length=25)
    employee_id = models.BigIntegerField(blank=True, null=True)
    employee_phone = models.CharField(max_length=30)
    employee_simcard = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_for_update'


class Salary(models.Model):
    company_id = models.CharField(max_length=25)
    employee_pin = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    employee_level = models.CharField(max_length=100)
    employee_position = models.CharField(max_length=100)
    employee_periode = models.CharField(max_length=6)
    employee_status = models.CharField(max_length=100)
    day_sal01 = models.IntegerField()
    day_sal02 = models.IntegerField()
    day_sal03 = models.IntegerField()
    day_sal04 = models.IntegerField()
    day_sal05 = models.IntegerField()
    day_sal06 = models.IntegerField()
    day_sal07 = models.IntegerField()
    day_sal08 = models.IntegerField()
    day_sal09 = models.IntegerField()
    day_sal10 = models.IntegerField()
    month_sal01 = models.CharField(max_length=100)
    month_sal02 = models.CharField(max_length=100)
    month_sal03 = models.CharField(max_length=100)
    month_sal04 = models.CharField(max_length=100)
    month_sal05 = models.CharField(max_length=100)
    month_sal06 = models.CharField(max_length=100)
    month_sal07 = models.CharField(max_length=100)
    month_sal08 = models.CharField(max_length=100)
    month_sal09 = models.CharField(max_length=100)
    month_sal10 = models.CharField(max_length=100)
    month_sal11 = models.CharField(max_length=100)
    month_sal12 = models.CharField(max_length=100)
    month_sal13 = models.CharField(max_length=100)
    month_sal14 = models.CharField(max_length=100)
    month_sal15 = models.CharField(max_length=100)
    month_sal16 = models.CharField(max_length=100)
    month_sal17 = models.CharField(max_length=100)
    month_sal18 = models.CharField(max_length=100)
    month_sal19 = models.CharField(max_length=100)
    month_sal20 = models.CharField(max_length=100)
    month_sal21 = models.CharField(max_length=100)
    month_sal22 = models.CharField(max_length=100)
    month_sal23 = models.CharField(max_length=100)
    month_sal24 = models.CharField(max_length=100)
    month_sal25 = models.CharField(max_length=100)
    month_sal26 = models.CharField(max_length=100)
    month_sal27 = models.CharField(max_length=100)
    month_sal28 = models.CharField(max_length=100)
    month_sal29 = models.CharField(max_length=100)
    month_sal30 = models.CharField(max_length=100)
    month_sal31 = models.CharField(max_length=100)
    month_sal32 = models.CharField(max_length=100)
    month_sal33 = models.CharField(max_length=100)
    month_sal34 = models.CharField(max_length=100)
    month_sal35 = models.CharField(max_length=100)
    month_sal36 = models.CharField(max_length=100)
    month_sal37 = models.CharField(max_length=100)
    month_sal38 = models.CharField(max_length=100)
    month_sal39 = models.CharField(max_length=100)
    month_sal40 = models.CharField(max_length=100)
    month_sal41 = models.CharField(max_length=100)
    month_sal42 = models.CharField(max_length=100)
    month_sal43 = models.CharField(max_length=100)
    month_sal44 = models.CharField(max_length=100)
    month_sal45 = models.CharField(max_length=100)
    month_sal46 = models.CharField(max_length=100)
    month_sal47 = models.CharField(max_length=100)
    month_sal48 = models.CharField(max_length=100)
    month_sal49 = models.CharField(max_length=100)
    month_sal50 = models.CharField(max_length=100)
    month_sal51 = models.CharField(max_length=100)
    month_sal52 = models.CharField(max_length=100)
    month_sal53 = models.CharField(max_length=100)
    month_sal54 = models.CharField(max_length=100)
    month_sal55 = models.CharField(max_length=100)
    month_sal56 = models.CharField(max_length=100)
    month_sal57 = models.CharField(max_length=100)
    month_sal58 = models.CharField(max_length=100)
    month_sal59 = models.CharField(max_length=100)
    month_sal60 = models.CharField(max_length=100)
    month_sal61 = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary'


class TAccount(models.Model):
    id_acc = models.IntegerField(primary_key=True)
    user_acc = models.CharField(max_length=50)
    pass_acc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_account'


class Users(models.Model):
    unique_id = models.CharField(unique=True, max_length=23)
    company_id = models.CharField(max_length=80)
    pin = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    encrypted_password = models.CharField(max_length=80)
    salt = models.CharField(max_length=10)
    authority = models.CharField(max_length=180, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
