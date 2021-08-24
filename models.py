# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminUser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AhcBrowsers(models.Model):
    bsr_id = models.PositiveIntegerField(primary_key=True)
    bsr_name = models.CharField(max_length=100)
    bsr_icon = models.CharField(max_length=50, blank=True, null=True)
    bsr_visits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_browsers'


class AhcCountries(models.Model):
    ctr_id = models.AutoField(primary_key=True)
    ctr_name = models.CharField(max_length=100)
    ctr_internet_code = models.CharField(max_length=5)
    ctr_latitude = models.CharField(max_length=30, blank=True, null=True)
    ctr_longitude = models.CharField(max_length=30, blank=True, null=True)
    ctr_visitors = models.IntegerField()
    ctr_visits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_countries'


class AhcDailyVisitorsStats(models.Model):
    vst_date = models.DateTimeField()
    vst_visitors = models.PositiveIntegerField(blank=True, null=True)
    vst_visits = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahc_daily_visitors_stats'


class AhcHits(models.Model):
    hit_id = models.AutoField(primary_key=True)
    hit_ip_address = models.CharField(max_length=50)
    hit_user_agent = models.CharField(max_length=200)
    hit_request_uri = models.CharField(max_length=200, blank=True, null=True)
    hit_page_id = models.CharField(max_length=30)
    hit_page_title = models.CharField(max_length=200, blank=True, null=True)
    ctr_id = models.PositiveIntegerField(blank=True, null=True)
    hit_referer = models.CharField(max_length=300, blank=True, null=True)
    hit_referer_site = models.CharField(max_length=100, blank=True, null=True)
    srh_id = models.PositiveIntegerField(blank=True, null=True)
    hit_search_words = models.CharField(max_length=200, blank=True, null=True)
    bsr_id = models.PositiveIntegerField()
    hit_date = models.DateField()
    hit_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ahc_hits'


class AhcKeywords(models.Model):
    kwd_id = models.AutoField(primary_key=True)
    kwd_ip_address = models.CharField(max_length=50)
    kwd_keywords = models.CharField(max_length=200)
    kwd_referer = models.CharField(max_length=300)
    srh_id = models.PositiveIntegerField()
    ctr_id = models.PositiveIntegerField(blank=True, null=True)
    bsr_id = models.PositiveIntegerField()
    kwd_date = models.DateField()
    kwd_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'ahc_keywords'


class AhcOnlineUsers(models.Model):
    hit_ip_address = models.CharField(max_length=50)
    hit_page_id = models.CharField(max_length=30)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ahc_online_users'


class AhcRecentVisitors(models.Model):
    vtr_id = models.AutoField(primary_key=True)
    vtr_ip_address = models.CharField(max_length=50)
    vtr_referer = models.CharField(max_length=300, blank=True, null=True)
    srh_id = models.PositiveIntegerField(blank=True, null=True)
    bsr_id = models.PositiveIntegerField()
    ctr_id = models.PositiveIntegerField(blank=True, null=True)
    vtr_date = models.DateField()
    vtr_time = models.TimeField()
    ahc_city = models.CharField(max_length=230, blank=True, null=True)
    ahc_region = models.CharField(max_length=230, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahc_recent_visitors'


class AhcReferingSites(models.Model):
    rfr_id = models.AutoField(primary_key=True)
    rfr_site_name = models.CharField(max_length=100)
    rfr_visits = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahc_refering_sites'


class AhcSearchEngineCrawlers(models.Model):
    bot_name = models.CharField(max_length=50)
    srh_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_search_engine_crawlers'


class AhcSearchEngines(models.Model):
    srh_id = models.AutoField(primary_key=True)
    srh_name = models.CharField(max_length=100)
    srh_query_parameter = models.CharField(max_length=10)
    srh_icon = models.CharField(max_length=50, blank=True, null=True)
    srh_identifier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahc_search_engines'


class AhcSearchingVisits(models.Model):
    vtsh_id = models.AutoField(primary_key=True)
    srh_id = models.PositiveIntegerField()
    vtsh_date = models.DateTimeField()
    vtsh_visits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_searching_visits'


class AhcSettings(models.Model):
    set_id = models.AutoField(primary_key=True)
    set_hits_days = models.PositiveIntegerField()
    set_ajax_check = models.PositiveIntegerField()
    set_ips = models.TextField(blank=True, null=True)
    set_google_map = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ahc_settings'


class AhcTitleTraffic(models.Model):
    til_id = models.AutoField(primary_key=True)
    til_page_id = models.CharField(max_length=30)
    til_page_title = models.CharField(max_length=100, blank=True, null=True)
    til_hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_title_traffic'


class AhcVisitors(models.Model):
    vst_id = models.AutoField(primary_key=True)
    vst_date = models.DateTimeField()
    vst_visitors = models.PositiveIntegerField(blank=True, null=True)
    vst_visits = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahc_visitors'


class AhcVisitsTime(models.Model):
    vtm_id = models.AutoField(primary_key=True)
    vtm_time_from = models.TimeField()
    vtm_time_to = models.TimeField()
    vtm_visitors = models.PositiveIntegerField()
    vtm_visits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ahc_visits_time'


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


class Bdlreimbursement(models.Model):
    doc_id = models.CharField(max_length=25, blank=True, null=True)
    budget_code = models.CharField(max_length=26, blank=True, null=True)
    bdldate = models.DateField(blank=True, null=True)
    start_km = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    finish_km = models.IntegerField(blank=True, null=True)
    curr = models.CharField(max_length=6, blank=True, null=True)
    bdl_perkm = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bdl_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bdl_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    destinationfrom = models.CharField(max_length=80, blank=True, null=True)
    destinationto = models.CharField(max_length=80, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    parking = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    toll = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    policeno = models.CharField(max_length=10, blank=True, null=True)
    carbrand = models.CharField(max_length=30, blank=True, null=True)
    cartype = models.CharField(max_length=30, blank=True, null=True)
    tips = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bensin = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    check1_sts = models.CharField(max_length=3, blank=True, null=True)
    check1_date = models.DateField(blank=True, null=True)
    check1_by = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bdlreimbursement'


class BdsManual(models.Model):
    paidto = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    spellnumber = models.TextField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    norek = models.CharField(max_length=25, blank=True, null=True)
    name_in_bank = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    prepare_by = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bds_manual'


class BulletinCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_commentmeta'


class BulletinComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_comments'


class BulletinGrpGooglePlace(models.Model):
    id = models.BigAutoField(primary_key=True)
    place_id = models.CharField(unique=True, max_length=80)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    updated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_grp_google_place'


class BulletinGrpGoogleReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    google_place_id = models.PositiveBigIntegerField()
    hash = models.CharField(unique=True, max_length=40)
    rating = models.IntegerField()
    text = models.CharField(max_length=10000, blank=True, null=True)
    time = models.IntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    profile_photo_url = models.CharField(max_length=255, blank=True, null=True)
    hide = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'bulletin_grp_google_review'


class BulletinLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bulletin_links'


class BulletinNextend2ImageStorage(models.Model):
    hash = models.CharField(unique=True, max_length=32)
    image = models.TextField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_image_storage'


class BulletinNextend2SectionStorage(models.Model):
    application = models.CharField(max_length=20)
    section = models.CharField(max_length=128)
    referencekey = models.CharField(max_length=128)
    value = models.TextField()
    system = models.IntegerField()
    editable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_section_storage'


class BulletinNextend2Smartslider3Generators(models.Model):
    group = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_smartslider3_generators'


class BulletinNextend2Smartslider3Sliders(models.Model):
    alias = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    params = models.TextField()
    time = models.DateTimeField()
    thumbnail = models.CharField(max_length=255)
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_smartslider3_sliders'


class BulletinNextend2Smartslider3SlidersXref(models.Model):
    group_id = models.IntegerField(primary_key=True)
    slider_id = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_smartslider3_sliders_xref'
        unique_together = (('group_id', 'slider_id'),)


class BulletinNextend2Smartslider3Slides(models.Model):
    title = models.CharField(max_length=200)
    slider = models.IntegerField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    published = models.IntegerField()
    first = models.IntegerField()
    slide = models.TextField(blank=True, null=True)
    description = models.TextField()
    thumbnail = models.CharField(max_length=255)
    params = models.TextField()
    ordering = models.IntegerField()
    generator_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_nextend2_smartslider3_slides'


class BulletinNinjaTableItems(models.Model):
    position = models.IntegerField(blank=True, null=True)
    table_id = models.IntegerField()
    owner_id = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=255)
    settings = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_ninja_table_items'


class BulletinOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bulletin_options'


class BulletinPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_postmeta'


class BulletinPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_posts'


class BulletinTermRelationships(models.Model):
    object_id = models.PositiveBigIntegerField(primary_key=True)
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class BulletinTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class BulletinTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_termmeta'


class BulletinTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bulletin_terms'


class BulletinUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_usermeta'


class BulletinUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'bulletin_users'


class BulletinWpgmza(models.Model):
    map_id = models.IntegerField()
    address = models.CharField(max_length=700)
    description = models.TextField()
    pic = models.CharField(max_length=700)
    link = models.CharField(max_length=2083)
    icon = models.CharField(max_length=700)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    anim = models.CharField(max_length=3)
    title = models.CharField(max_length=700)
    infoopen = models.CharField(max_length=3)
    category = models.CharField(max_length=500)
    approved = models.IntegerField(blank=True, null=True)
    retina = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    did = models.CharField(max_length=500)
    sticky = models.IntegerField(blank=True, null=True)
    other_data = models.TextField()
    latlng = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza'


class BulletinWpgmzaCircles(models.Model):
    map_id = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    radius = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=16, blank=True, null=True)
    opacity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza_circles'


class BulletinWpgmzaMaps(models.Model):
    map_title = models.CharField(max_length=55)
    map_width = models.CharField(max_length=6)
    map_height = models.CharField(max_length=6)
    map_start_lat = models.CharField(max_length=700)
    map_start_lng = models.CharField(max_length=700)
    map_start_location = models.CharField(max_length=700)
    map_start_zoom = models.IntegerField()
    default_marker = models.CharField(max_length=700)
    type = models.IntegerField()
    alignment = models.IntegerField()
    directions_enabled = models.IntegerField()
    styling_enabled = models.IntegerField()
    styling_json = models.TextField()
    active = models.IntegerField()
    kml = models.CharField(max_length=700)
    bicycle = models.IntegerField()
    traffic = models.IntegerField()
    dbox = models.IntegerField()
    dbox_width = models.CharField(max_length=10)
    listmarkers = models.IntegerField()
    listmarkers_advanced = models.IntegerField()
    filterbycat = models.IntegerField()
    ugm_enabled = models.IntegerField()
    ugm_category_enabled = models.IntegerField()
    fusion = models.CharField(max_length=100)
    map_width_type = models.CharField(max_length=3)
    map_height_type = models.CharField(max_length=3)
    mass_marker_support = models.IntegerField()
    ugm_access = models.IntegerField()
    order_markers_by = models.IntegerField()
    order_markers_choice = models.IntegerField()
    show_user_location = models.IntegerField()
    default_to = models.CharField(max_length=700)
    other_settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza_maps'


class BulletinWpgmzaPolygon(models.Model):
    map_id = models.IntegerField()
    polydata = models.TextField()
    description = models.TextField()
    innerpolydata = models.TextField()
    linecolor = models.CharField(max_length=7)
    lineopacity = models.CharField(max_length=7)
    fillcolor = models.CharField(max_length=7)
    opacity = models.CharField(max_length=3)
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=700)
    ohfillcolor = models.CharField(max_length=7)
    ohlinecolor = models.CharField(max_length=7)
    ohopacity = models.CharField(max_length=3)
    polyname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza_polygon'


class BulletinWpgmzaPolylines(models.Model):
    map_id = models.IntegerField()
    polydata = models.TextField()
    linecolor = models.CharField(max_length=7)
    linethickness = models.CharField(max_length=3)
    opacity = models.CharField(max_length=3)
    polyname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza_polylines'


class BulletinWpgmzaRectangles(models.Model):
    map_id = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    cornera = models.TextField(db_column='cornerA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cornerb = models.TextField(db_column='cornerB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    color = models.CharField(max_length=16, blank=True, null=True)
    opacity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_wpgmza_rectangles'


class BulletinYoastSeoLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    post_id = models.PositiveBigIntegerField()
    target_post_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'bulletin_yoast_seo_links'


class BulletinYoastSeoMeta(models.Model):
    object_id = models.PositiveBigIntegerField(unique=True)
    internal_link_count = models.PositiveIntegerField(blank=True, null=True)
    incoming_link_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulletin_yoast_seo_meta'


class Businesstriptransaction(models.Model):
    budget_code = models.CharField(max_length=30, blank=True, null=True)
    doc_id = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    component = models.CharField(max_length=100, blank=True, null=True)
    transaction_dt = models.DateField(blank=True, null=True)
    curr = models.CharField(max_length=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businesstriptransaction'


class CbtModules(models.Model):
    mod = models.CharField(max_length=10, blank=True, null=True)
    link = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    topics = models.IntegerField(blank=True, null=True)
    admin = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbt_modules'


class CbtRegulation(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbt_regulation'


class CbtTransaction(models.Model):
    mod_id = models.IntegerField(blank=True, null=True)
    emp_no = models.CharField(max_length=50, blank=True, null=True)
    lates_open = models.DateTimeField(blank=True, null=True)
    begin_open = models.DateTimeField(blank=True, null=True)
    lates_test = models.DateTimeField(blank=True, null=True)
    result_test = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    result_time = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status_active = models.IntegerField(blank=True, null=True)
    status_access = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbt_transaction'


class CollectiveLeave(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    period = models.CharField(max_length=4, blank=True, null=True)
    wk_day = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collective_leave'


class CooMember(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    emp_no = models.CharField(max_length=35, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    member_sts = models.CharField(max_length=3, blank=True, null=True)
    simpanan_pokok = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iuran_sukarela = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iuran_wajib = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coo_member'


class CooTransaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    period = models.CharField(max_length=6, blank=True, null=True)
    emp_no = models.CharField(max_length=35, blank=True, null=True)
    pokok = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wajib = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sukarela = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_pokok = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_wajib = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_sukarela = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_pokok = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_wajib = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_sukarela = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remain_pokok = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remain_wajib = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remain_sukarela = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    belanja_toko = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_cicilan1 = models.IntegerField(blank=True, null=True)
    cicilan_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tenor_1 = models.IntegerField(blank=True, null=True)
    cicilan_1_str = models.CharField(max_length=30, blank=True, null=True)
    id_cicilan2 = models.IntegerField(blank=True, null=True)
    cicilan_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tenor_2 = models.IntegerField(blank=True, null=True)
    cicilan_2_str = models.CharField(max_length=30, blank=True, null=True)
    id_cicilan3 = models.IntegerField(blank=True, null=True)
    cicilan_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tenor_3 = models.IntegerField(blank=True, null=True)
    cicilan_3_str = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coo_transaction'


class CooTransactionDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    emp_no = models.CharField(max_length=35, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coo_transaction_detail'


class DefaultBdl(models.Model):
    emp_no = models.CharField(max_length=30, blank=True, null=True)
    police_number = models.CharField(max_length=30, blank=True, null=True)
    car_brand = models.CharField(max_length=30, blank=True, null=True)
    car_type = models.CharField(max_length=30, blank=True, null=True)
    destination_from = models.CharField(max_length=100, blank=True, null=True)
    destination_to = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_bdl'


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


class EmployeeGroupatt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    group_id = models.CharField(max_length=4)
    emp_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'employee_groupatt'
        unique_together = (('group_id', 'emp_no'),)


class Entertainment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    doc_id = models.CharField(max_length=50, blank=True, null=True)
    budget_code = models.CharField(max_length=50, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ent_dt = models.DateField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_position = models.CharField(max_length=255, blank=True, null=True)
    customer_company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entertainment'


class Groupusers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groupusers'


class HmsiCopChecklist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emp_no = models.CharField(max_length=25)
    cop_status = models.CharField(max_length=3, blank=True, null=True)
    stnk_status = models.CharField(max_length=3, blank=True, null=True)
    bpkb_status = models.CharField(max_length=3, blank=True, null=True)
    car_insurance = models.CharField(max_length=3, blank=True, null=True)
    live_insurance = models.CharField(max_length=3, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    supporting_docs = models.TextField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    ins_due_date = models.DateField(blank=True, null=True)
    last_sent = models.DateTimeField(blank=True, null=True)
    sts_send = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmsi_cop_checklist'


class HmsiCopymachine(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    emp_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'hmsi_copymachine'
        unique_together = (('id', 'emp_no'),)


class Hranswer(models.Model):
    id_question = models.IntegerField()
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hranswer'


class Hrquestion(models.Model):
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    question_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrquestion'


class InsurResult(models.Model):
    comment = models.CharField(max_length=70, blank=True, null=True)
    emp_no = models.CharField(primary_key=True, max_length=50)
    result_insur = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insur_result'


class Jinglefamilyday(models.Model):
    emp_no = models.CharField(max_length=30, blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jinglefamilyday'


class LeaveAdjustment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    period = models.CharField(max_length=4, blank=True, null=True)
    valid_dt = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    emp_no = models.CharField(max_length=50, blank=True, null=True)
    adjustment_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_adjustment'


class Leavedetail(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=50)
    wk_day = models.CharField(max_length=8)
    wk_type = models.CharField(max_length=3)
    act_state = models.CharField(max_length=3, blank=True, null=True)
    emp_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'leavedetail'
        unique_together = (('ref_id', 'wk_day', 'wk_type', 'emp_no'),)


class Leaveheader(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=24)
    annual_period = models.CharField(max_length=4)
    emp_no = models.CharField(max_length=15)
    from_dt = models.CharField(max_length=8)
    finish_dt = models.CharField(max_length=8)
    wk_type = models.CharField(max_length=3)
    in_time = models.TimeField()
    out_time = models.TimeField()
    loss_time = models.IntegerField()
    plan_in = models.TimeField()
    plan_out = models.TimeField()
    term_days = models.IntegerField()
    reason = models.TextField()
    destination = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    crt_dt = models.DateField()
    upd_dt = models.DateField()
    user_id = models.CharField(max_length=7)
    approver_1 = models.CharField(max_length=15)
    approver_2 = models.CharField(max_length=15)
    approver_3 = models.CharField(max_length=15)
    act_key = models.CharField(max_length=100)
    del_key = models.CharField(max_length=100)
    send_id = models.FloatField(blank=True, null=True)
    sendapp1_sts = models.CharField(max_length=3)
    sendapp1_dt = models.DateTimeField()
    sendapp2_sts = models.CharField(max_length=3)
    sendapp2_dt = models.DateTimeField()
    sendapp3_sts = models.CharField(max_length=3)
    sendapp3_dt = models.DateTimeField()
    sendemp_sts = models.CharField(max_length=3)
    act_term = models.IntegerField()
    act_state1 = models.CharField(max_length=3)
    act_comment1 = models.CharField(max_length=255, blank=True, null=True)
    act_date1 = models.DateTimeField()
    act_state2 = models.CharField(max_length=3)
    act_comment2 = models.CharField(max_length=255, blank=True, null=True)
    act_date2 = models.DateTimeField()
    act_state3 = models.CharField(max_length=3)
    act_comment3 = models.CharField(max_length=255, blank=True, null=True)
    act_date3 = models.DateTimeField()
    attachment = models.CharField(max_length=50)
    doc_support = models.CharField(max_length=3)
    acc_step = models.IntegerField()
    status = models.CharField(max_length=5, blank=True, null=True)
    leavedir = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaveheader'


class LogbookLayer(models.Model):
    doc_type = models.IntegerField()
    layer = models.IntegerField()
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    div = models.CharField(max_length=25, blank=True, null=True)
    alias_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbook_layer'


class Logbookanswer(models.Model):
    id_question = models.IntegerField()
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbookanswer'


class Logbookbudget(models.Model):
    doc_id = models.CharField(max_length=20)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    budget_code = models.CharField(max_length=30)
    gl_name = models.CharField(max_length=50)
    curr = models.CharField(max_length=7, blank=True, null=True)
    amt = models.FloatField()
    remark = models.CharField(max_length=200)
    gl_no = models.CharField(max_length=30)
    div_code = models.CharField(max_length=30)
    div_budget = models.CharField(max_length=30)
    fy = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'logbookbudget'


class Logbookdetail(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    doc_id = models.CharField(max_length=50)
    sort_id = models.IntegerField()
    userid = models.CharField(max_length=25, blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    send_date = models.DateTimeField(blank=True, null=True)
    send_to = models.CharField(max_length=25, blank=True, null=True)
    send_to_user = models.CharField(max_length=25, blank=True, null=True)
    received_by = models.CharField(max_length=25, blank=True, null=True)
    received_by_user = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    term_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbookdetail'


class Logbookheader(models.Model):
    doc_id = models.CharField(primary_key=True, max_length=20)
    doc_status = models.CharField(max_length=20, blank=True, null=True)
    doc_type = models.IntegerField()
    doc_date = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=25, blank=True, null=True)
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    doc_remark = models.TextField(blank=True, null=True)
    doc_amount_idr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_usd = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_ypn = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_bath = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_myr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_sgd = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    doc_amount_euro = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    current_doc_sts = models.CharField(max_length=10, blank=True, null=True)
    received_dt = models.DateTimeField(blank=True, null=True)
    send_dt = models.DateTimeField(blank=True, null=True)
    sending_to = models.CharField(max_length=25, blank=True, null=True)
    sending_from = models.CharField(max_length=25, blank=True, null=True)
    sending_to_user = models.CharField(max_length=25, blank=True, null=True)
    sending_from_user = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=30, blank=True, null=True)
    bank_no = models.CharField(max_length=25, blank=True, null=True)
    name_payment = models.CharField(max_length=50, blank=True, null=True)
    pum_amount_idr = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_usd = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_ypn = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_bath = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_myr = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_sgd = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pum_amount_euro = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    total_payment_idr = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    total_payment_usd = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_payment_ypn = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_payment_bath = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_payment_myr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_payment_sgd = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_payment_euro = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_remark = models.CharField(max_length=255, blank=True, null=True)
    logbookdir = models.CharField(max_length=255, blank=True, null=True)
    act_state1 = models.CharField(max_length=3, blank=True, null=True)
    act_date1 = models.DateField(blank=True, null=True)
    act_state2 = models.CharField(max_length=3, blank=True, null=True)
    act_date2 = models.DateField(blank=True, null=True)
    act_state3 = models.CharField(max_length=3, blank=True, null=True)
    act_date3 = models.DateField(blank=True, null=True)
    act_state4 = models.CharField(max_length=3, blank=True, null=True)
    act_date4 = models.DateField(blank=True, null=True)
    act_state5 = models.CharField(max_length=3, blank=True, null=True)
    act_date5 = models.DateField(blank=True, null=True)
    act_state6 = models.CharField(max_length=3, blank=True, null=True)
    act_date6 = models.DateField(blank=True, null=True)
    act_state7 = models.CharField(max_length=3, blank=True, null=True)
    act_date7 = models.DateField(blank=True, null=True)
    act_state8 = models.CharField(max_length=3, blank=True, null=True)
    act_date8 = models.DateField(blank=True, null=True)
    act_state9 = models.CharField(max_length=3, blank=True, null=True)
    act_date9 = models.DateField(blank=True, null=True)
    act_state10 = models.CharField(max_length=3, blank=True, null=True)
    act_date10 = models.DateField(blank=True, null=True)
    approver_1 = models.CharField(max_length=25, blank=True, null=True)
    approver_2 = models.CharField(max_length=25, blank=True, null=True)
    approver_3 = models.CharField(max_length=25, blank=True, null=True)
    approver_4 = models.CharField(max_length=25, blank=True, null=True)
    approver_5 = models.CharField(max_length=25, blank=True, null=True)
    approver_6 = models.CharField(max_length=25, blank=True, null=True)
    approver_7 = models.CharField(max_length=25, blank=True, null=True)
    approver_8 = models.CharField(max_length=25, blank=True, null=True)
    approver_9 = models.CharField(max_length=25, blank=True, null=True)
    approver_10 = models.CharField(max_length=25, blank=True, null=True)
    act_key = models.TextField(blank=True, null=True)
    act_term = models.IntegerField(blank=True, null=True)
    act_comment1 = models.TextField(blank=True, null=True)
    act_comment2 = models.TextField(blank=True, null=True)
    act_comment3 = models.TextField(blank=True, null=True)
    act_comment4 = models.TextField(blank=True, null=True)
    act_comment5 = models.TextField(blank=True, null=True)
    act_comment6 = models.TextField(blank=True, null=True)
    act_comment7 = models.TextField(blank=True, null=True)
    act_comment8 = models.TextField(blank=True, null=True)
    act_comment9 = models.TextField(blank=True, null=True)
    act_comment10 = models.TextField(blank=True, null=True)
    sts_new = models.CharField(max_length=1, blank=True, null=True)
    sppd_bumber = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbookheader'


class Logbookquestion(models.Model):
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    question_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    doc_id = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logbookquestion'


class MasterActivity(models.Model):
    type_activity = models.CharField(max_length=30, blank=True, null=True)
    activity_detail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_activity'


class MasterAllowance(models.Model):
    level = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    curr = models.CharField(max_length=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_allowance'


class MasterAtttype(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=5)  # Field name made lowercase.
    typename = models.CharField(max_length=50, blank=True, null=True)
    typedesc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_atttype'


class MasterBudget(models.Model):
    budget_number = models.CharField(primary_key=True, max_length=30)
    div_code = models.CharField(max_length=30)
    gl_no = models.CharField(max_length=30)
    gl_name = models.CharField(max_length=50)
    detail_activity_name = models.TextField()
    division_budget = models.CharField(max_length=30)
    fy = models.CharField(max_length=4)
    remain_budget = models.FloatField()
    remark = models.TextField()
    no = models.IntegerField()
    activity_code = models.CharField(max_length=30)
    detail_activity_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'master_budget'
        unique_together = (('budget_number', 'div_code', 'gl_no'),)


class MasterBusinesstripcom(models.Model):
    component = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_businesstripcom'


class MasterCity(models.Model):
    kode_kota = models.AutoField(primary_key=True)
    kode_propinsi = models.IntegerField()
    nama_kota = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_city'


class MasterCollectiveleave(models.Model):
    yyyy = models.CharField(primary_key=True, max_length=4)
    wk_day = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'master_collectiveleave'
        unique_together = (('yyyy', 'wk_day'),)


class MasterCombenResult(models.Model):
    id_status = models.AutoField(primary_key=True)
    status_result = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_comben_result'


class MasterDepartment(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=6)
    dept_name = models.CharField(max_length=50)
    crt_dt = models.DateTimeField()
    upd_dt = models.DateTimeField()
    user_id = models.CharField(max_length=15)
    division_id = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'master_department'
        unique_together = (('dept_id', 'division_id'),)


class MasterDivision(models.Model):
    division_id = models.CharField(primary_key=True, max_length=3)
    division_name = models.CharField(max_length=50)
    crt_dt = models.DateTimeField()
    upd_dt = models.DateTimeField()
    user_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'master_division'


class MasterDoctype(models.Model):
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    active_sts = models.CharField(max_length=1, blank=True, null=True)
    pic_division = models.CharField(max_length=255, blank=True, null=True)
    pic_id = models.CharField(max_length=255, blank=True, null=True)
    action_detail = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_doctype'


class MasterEmployee(models.Model):
    emp_no = models.CharField(primary_key=True, max_length=18)
    emp_name = models.CharField(max_length=100)
    ent_dt = models.CharField(max_length=8, blank=True, null=True)
    contract_dt = models.CharField(max_length=8, blank=True, null=True)
    location_code = models.CharField(max_length=10, blank=True, null=True)
    division_code = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=50)
    section_code = models.CharField(max_length=50)
    no_kk = models.CharField(max_length=30, blank=True, null=True)
    no_ktp = models.CharField(max_length=30, blank=True, null=True)
    npwp = models.CharField(max_length=15, blank=True, null=True)
    bank_acct = models.CharField(max_length=30, blank=True, null=True)
    birth_place = models.CharField(max_length=80, blank=True, null=True)
    birth_dt = models.CharField(max_length=8, blank=True, null=True)
    married_sts = models.CharField(max_length=1, blank=True, null=True)
    married_dt = models.CharField(max_length=8, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    rt_1 = models.CharField(max_length=3, blank=True, null=True)
    rw_1 = models.CharField(max_length=3, blank=True, null=True)
    kelurahan_1 = models.CharField(max_length=50, blank=True, null=True)
    kecamatan_1 = models.CharField(max_length=50, blank=True, null=True)
    home_phone = models.CharField(max_length=25, blank=True, null=True)
    mobile_phone = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    update_dt = models.DateTimeField(blank=True, null=True)
    key_number = models.CharField(max_length=255, blank=True, null=True)
    key_token = models.CharField(max_length=255, blank=True, null=True)
    confirm_dt = models.DateField(blank=True, null=True)
    mail_add = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    adminid1 = models.CharField(max_length=18, blank=True, null=True)
    adminid2 = models.CharField(max_length=18, blank=True, null=True)
    adminid3 = models.CharField(max_length=18, blank=True, null=True)
    adminid4 = models.CharField(max_length=18, blank=True, null=True)
    adminid5 = models.CharField(max_length=18, blank=True, null=True)
    adminid6 = models.CharField(max_length=18, blank=True, null=True)
    approverid1 = models.CharField(max_length=18, blank=True, null=True)
    approverid2 = models.CharField(max_length=18, blank=True, null=True)
    approverid3 = models.CharField(max_length=255, blank=True, null=True)
    approverid4 = models.CharField(max_length=18, blank=True, null=True)
    approverid5 = models.CharField(max_length=255, blank=True, null=True)
    approverid6 = models.CharField(max_length=18, blank=True, null=True)
    app4validfrom = models.DateField(blank=True, null=True)
    app4validto = models.DateField(blank=True, null=True)
    app5validfrom = models.DateField(blank=True, null=True)
    app5validto = models.DateField(blank=True, null=True)
    lvl_cd = models.IntegerField()
    job_title_cd = models.CharField(max_length=5)
    user_type = models.CharField(max_length=5, blank=True, null=True)
    budget_code = models.CharField(max_length=15, blank=True, null=True)
    budget_code2 = models.CharField(max_length=15, blank=True, null=True)
    budget_code3 = models.CharField(max_length=15, blank=True, null=True)
    status_emp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_employee'


class MasterEmployeeGroupwa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    group_id = models.CharField(max_length=2)
    emp_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'master_employee_groupwa'
        unique_together = (('group_id', 'emp_no'),)


class MasterFamily(models.Model):
    emp_no = models.CharField(max_length=25)
    relation = models.CharField(max_length=1, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    fam_name = models.CharField(max_length=50, blank=True, null=True)
    fam_birth_dt = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_family'


class MasterGroupatt(models.Model):
    group_id = models.CharField(primary_key=True, max_length=4)
    group_name = models.CharField(max_length=50)
    group_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_groupatt'


class MasterInterviewResult(models.Model):
    id_status = models.AutoField(primary_key=True)
    status_result = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_interview_result'


class MasterLeavetype(models.Model):
    lv_type = models.CharField(primary_key=True, max_length=5)
    type_name = models.CharField(db_column='Type_name', max_length=50)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    term = models.IntegerField()
    blc_show = models.CharField(max_length=3)
    visibilty_sts = models.CharField(max_length=3)
    call_blc = models.CharField(max_length=3)
    doc_support = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'master_leavetype'


class MasterLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_level'


class MasterLocation(models.Model):
    id_location = models.CharField(db_column='Id_location', primary_key=True, max_length=3)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_name', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crt_dt = models.DateTimeField()
    upd_dt = models.DateTimeField()
    user_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'master_location'


class MasterMcuProvider(models.Model):
    provider = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_mcu_provider'


class MasterMcuResult(models.Model):
    id_status = models.AutoField(primary_key=True)
    status_result = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_mcu_result'


class MasterProvince(models.Model):
    kode_propinsi = models.AutoField(primary_key=True)
    nama_propinsi = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_province'


class MasterPsychotestResult(models.Model):
    id_status = models.AutoField(primary_key=True)
    status_result = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_psychotest_result'


class MasterRecruitmentScreening(models.Model):
    name_screening = models.CharField(max_length=30, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_recruitment_screening'


class MasterTitle(models.Model):
    title_id = models.CharField(primary_key=True, max_length=10)
    title_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_title'


class MasterVanue(models.Model):
    id_vanue = models.AutoField(primary_key=True)
    vanue_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_vanue'


class MasterWorkingtype(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=3)  # Field name made lowercase.
    typename = models.CharField(max_length=50, blank=True, null=True)
    typedesc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_workingtype'


class McuResult(models.Model):
    emp_no = models.CharField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcu_result'


class Medicaldir(models.Model):
    doc_id = models.CharField(max_length=25, blank=True, null=True)
    dirreceipt = models.CharField(max_length=255, blank=True, null=True)
    relation_id = models.IntegerField(blank=True, null=True)
    check1_sts = models.CharField(max_length=1, blank=True, null=True)
    check1_by = models.CharField(max_length=25, blank=True, null=True)
    check1_date = models.DateField(blank=True, null=True)
    check1_comment = models.TextField(blank=True, null=True)
    check2_sts = models.CharField(max_length=1, blank=True, null=True)
    check2_by = models.CharField(max_length=25, blank=True, null=True)
    check2_date = models.DateField(blank=True, null=True)
    check2_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicaldir'


class Medicalperiod(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    yyyymm = models.CharField(max_length=6)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicalperiod'


class Medicalreimbursement(models.Model):
    doc_id = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    emp_no = models.CharField(max_length=25, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    curr = models.CharField(max_length=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fam_name = models.CharField(max_length=50, blank=True, null=True)
    relation = models.CharField(max_length=1, blank=True, null=True)
    receipt_dt = models.DateField(blank=True, null=True)
    diagnosa = models.CharField(max_length=100, blank=True, null=True)
    notes_doctor = models.TextField(blank=True, null=True)
    payment_sts = models.CharField(max_length=5, blank=True, null=True)
    payment_period = models.CharField(max_length=6, blank=True, null=True)
    sortdoc = models.IntegerField(blank=True, null=True)
    sortreceipt = models.IntegerField(blank=True, null=True)
    check1_sts = models.CharField(max_length=1, blank=True, null=True)
    check1_by = models.CharField(max_length=25, blank=True, null=True)
    check1_date = models.DateField(blank=True, null=True)
    check1_comment = models.TextField(blank=True, null=True)
    check2_sts = models.CharField(max_length=1, blank=True, null=True)
    check2_by = models.CharField(max_length=25, blank=True, null=True)
    check2_date = models.DateField(blank=True, null=True)
    check2_comment = models.TextField(blank=True, null=True)
    dir_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicalreimbursement'


class MenusAutho(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    group_id = models.IntegerField(blank=True, null=True)
    main_menus_id = models.IntegerField(blank=True, null=True)
    sub_menus_id = models.IntegerField(blank=True, null=True)
    sub_sub_menus_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus_autho'


class MenusMain(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    menus_name = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    sub = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus_main'


class Mynotification(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    notif_name = models.CharField(max_length=50, blank=True, null=True)
    label_htm = models.CharField(max_length=50, blank=True, null=True)
    module = models.CharField(max_length=40, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mynotification'


class Notification(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    emp_no = models.CharField(max_length=50, blank=True, null=True)
    notif_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'


class Overtimeperiod(models.Model):
    period = models.CharField(primary_key=True, max_length=6)
    status = models.CharField(max_length=1)
    closing_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'overtimeperiod'


class Overtimerequest(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=18)
    group_key = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=6)
    emp_no = models.CharField(max_length=15)
    wk_day = models.CharField(max_length=8)
    wk_type = models.CharField(max_length=1)
    start_date = models.TimeField(blank=True, null=True)
    end_date = models.TimeField(blank=True, null=True)
    actual_from = models.TimeField(blank=True, null=True)
    actual_end = models.TimeField(blank=True, null=True)
    plan_from = models.TimeField(blank=True, null=True)
    plan_to = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    real_ot = models.DecimalField(max_digits=10, decimal_places=2)
    act_state1 = models.CharField(max_length=3, blank=True, null=True)
    act_state1_key = models.CharField(max_length=255, blank=True, null=True)
    act_comment1 = models.CharField(max_length=255, blank=True, null=True)
    act_date1 = models.DateTimeField(blank=True, null=True)
    act_state2 = models.CharField(max_length=3, blank=True, null=True)
    act_state2_key = models.CharField(max_length=255, blank=True, null=True)
    act_comment2 = models.CharField(max_length=255, blank=True, null=True)
    act_date2 = models.DateTimeField(blank=True, null=True)
    act_state3 = models.CharField(max_length=3, blank=True, null=True)
    act_comment3 = models.CharField(max_length=255, blank=True, null=True)
    act_date3 = models.DateTimeField(blank=True, null=True)
    approver_1 = models.CharField(max_length=15, blank=True, null=True)
    approver_2 = models.CharField(max_length=15)
    approver_3 = models.CharField(max_length=15, blank=True, null=True)
    act_key = models.CharField(max_length=50, blank=True, null=True)
    del_key = models.CharField(max_length=100, blank=True, null=True)
    crt_dt = models.DateField(blank=True, null=True)
    upd_dt = models.DateField(blank=True, null=True)
    user_id = models.CharField(max_length=15, blank=True, null=True)
    proposed_by = models.CharField(max_length=25, blank=True, null=True)
    send_id = models.FloatField(blank=True, null=True)
    sendapp1_sts = models.CharField(max_length=3, blank=True, null=True)
    sendapp1_dt = models.DateTimeField(blank=True, null=True)
    sendapp2_sts = models.CharField(max_length=3, blank=True, null=True)
    sendapp2_dt = models.DateTimeField(blank=True, null=True)
    sendapp3_sts = models.CharField(max_length=3, blank=True, null=True)
    sendapp3_dt = models.DateTimeField(blank=True, null=True)
    sendemp_sts = models.CharField(max_length=3, blank=True, null=True)
    app_remark = models.CharField(max_length=100, blank=True, null=True)
    acc_step = models.IntegerField(blank=True, null=True)
    act_term = models.IntegerField(blank=True, null=True)
    submit_sts = models.CharField(max_length=3)
    act_state1_actual = models.CharField(max_length=3, blank=True, null=True)
    act_state1_key_actual = models.CharField(max_length=50, blank=True, null=True)
    act_date1_actual = models.DateTimeField(blank=True, null=True)
    act_comment1_actual = models.TextField(blank=True, null=True)
    act_state2_actual = models.CharField(max_length=3, blank=True, null=True)
    act_state2_key_actual = models.CharField(max_length=50, blank=True, null=True)
    act_date2_actual = models.DateTimeField(blank=True, null=True)
    act_comment2_actual = models.TextField(blank=True, null=True)
    act_state3_actual = models.CharField(max_length=3, blank=True, null=True)
    act_date3_actual = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    app_emp = models.CharField(max_length=3, blank=True, null=True)
    app_emp_date = models.DateTimeField(blank=True, null=True)
    ga_sts = models.CharField(max_length=3, blank=True, null=True)
    app_time_in = models.TimeField(blank=True, null=True)
    app_time_out = models.TimeField(blank=True, null=True)
    process_type = models.CharField(max_length=5, blank=True, null=True)
    paid_status = models.CharField(max_length=5, blank=True, null=True)
    recall_status = models.CharField(max_length=1, blank=True, null=True)
    time_type = models.CharField(max_length=5, blank=True, null=True)
    real_ot_actual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    type_activity = models.CharField(max_length=30, blank=True, null=True)
    activity_detail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'overtimerequest'


class RecruitmentCandidatefamily(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    fam_name = models.CharField(max_length=50, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    relation = models.CharField(max_length=30, blank=True, null=True)
    pendidikan = models.CharField(max_length=30, blank=True, null=True)
    jk = models.CharField(max_length=30, blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    perusahaan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_candidatefamily'


class RecruitmentCandidates(models.Model):
    id_candidate = models.AutoField(primary_key=True)
    vacant_id = models.IntegerField()
    candidate_name = models.CharField(max_length=50)
    email_add = models.CharField(max_length=30, blank=True, null=True)
    phone_hp = models.CharField(max_length=30, blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    current_status = models.IntegerField(blank=True, null=True)
    screening_status = models.IntegerField(blank=True, null=True)
    start_screening = models.DateTimeField(blank=True, null=True)
    finish_screening = models.DateTimeField(blank=True, null=True)
    psychotest_status = models.IntegerField(blank=True, null=True)
    start_psychotest = models.DateTimeField(blank=True, null=True)
    finish_psychotest = models.DateTimeField(blank=True, null=True)
    inteview_status = models.IntegerField(blank=True, null=True)
    start_interview = models.DateTimeField(blank=True, null=True)
    finish_interview = models.DateTimeField(blank=True, null=True)
    comben_status = models.IntegerField(blank=True, null=True)
    start_comben = models.DateTimeField(blank=True, null=True)
    finish_comben = models.DateTimeField(blank=True, null=True)
    mcu_status = models.IntegerField(blank=True, null=True)
    start_mcu = models.DateTimeField(blank=True, null=True)
    finish_mcu = models.DateTimeField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)
    pic_now = models.CharField(max_length=30, blank=True, null=True)
    cvdir = models.CharField(max_length=200, blank=True, null=True)
    ssn = models.CharField(max_length=255, blank=True, null=True)
    place_birth = models.CharField(max_length=50, blank=True, null=True)
    birth_dt = models.DateField(blank=True, null=True)
    add_ssn = models.TextField(blank=True, null=True)
    add_dms = models.TextField(blank=True, null=True)
    phone_home = models.CharField(max_length=25, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    tinggi_badan = models.IntegerField(blank=True, null=True)
    berat_badan = models.IntegerField(blank=True, null=True)
    married_sts = models.CharField(max_length=3, blank=True, null=True)
    sim_number = models.CharField(max_length=35, blank=True, null=True)
    religion = models.CharField(max_length=3, blank=True, null=True)
    home_sts = models.CharField(max_length=5, blank=True, null=True)
    vehicle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_candidates'
        unique_together = (('id_candidate', 'vacant_id'),)


class RecruitmentComben(models.Model):
    id_comben = models.AutoField(primary_key=True)
    id_candidate = models.IntegerField()
    activity = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    start_comben = models.DateField(blank=True, null=True)
    finish_comben = models.DateField(blank=True, null=True)
    combendir = models.CharField(max_length=300, blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_comben'
        unique_together = (('id_comben', 'id_candidate'),)


class RecruitmentInterview(models.Model):
    id_interview = models.AutoField(primary_key=True)
    id_candidate = models.IntegerField()
    interviewer = models.CharField(max_length=50)
    status = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    interview_time = models.TimeField(blank=True, null=True)
    vanue = models.CharField(max_length=100, blank=True, null=True)
    interviewdir = models.CharField(max_length=300, blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_interview'
        unique_together = (('id_interview', 'id_candidate'),)


class RecruitmentMcu(models.Model):
    id_mcu = models.AutoField(primary_key=True)
    id_candidate = models.IntegerField()
    provider = models.CharField(max_length=50)
    status = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    start_mcu = models.DateField(blank=True, null=True)
    finish_mcu = models.DateField(blank=True, null=True)
    mcudir = models.CharField(max_length=300, blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_mcu'
        unique_together = (('id_mcu', 'id_candidate'),)


class RecruitmentPsychotest(models.Model):
    id_psychotest = models.AutoField(primary_key=True)
    id_candidate = models.IntegerField()
    provider = models.CharField(max_length=50)
    status = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    start_psychotest = models.DateField(blank=True, null=True)
    finish_psychotest = models.DateField(blank=True, null=True)
    psychotestdir = models.CharField(max_length=300, blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_psychotest'
        unique_together = (('id_psychotest', 'id_candidate'),)


class RecruitmentVacancies(models.Model):
    level = models.IntegerField(blank=True, null=True)
    job_title_id = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)
    vacancy_name = models.CharField(max_length=50, blank=True, null=True)
    no_of_vacanct = models.IntegerField(blank=True, null=True)
    remain = models.IntegerField(blank=True, null=True)
    division_id = models.CharField(max_length=255, blank=True, null=True)
    fy = models.CharField(max_length=4, blank=True, null=True)
    status_budget = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    job_desc = models.TextField(blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)
    upd_dt = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    ptkdir = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_vacancies'


class Sendinghistory(models.Model):
    sendingfrom = models.CharField(max_length=25, blank=True, null=True)
    sendingto = models.CharField(max_length=25, blank=True, null=True)
    sendingtoemail = models.CharField(max_length=50, blank=True, null=True)
    sendingkey = models.TextField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    sendingdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sendinghistory'


class SettingSystem(models.Model):
    setting_name = models.CharField(max_length=25, blank=True, null=True)
    string_val1 = models.CharField(max_length=25, blank=True, null=True)
    string_val2 = models.CharField(max_length=25, blank=True, null=True)
    string_val3 = models.CharField(max_length=25, blank=True, null=True)
    int_val1 = models.IntegerField(blank=True, null=True)
    int_val2 = models.IntegerField(blank=True, null=True)
    int_val3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setting_system'


class SubSubmenus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    submenus_id = models.IntegerField(blank=True, null=True)
    submenus_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    label_htm = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_submenus'


class Submenus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    menus_id = models.IntegerField(blank=True, null=True)
    submenus_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    label_htm = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submenus'


class SysUtility(models.Model):
    id_cd = models.AutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    ad_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_utility'


class TCbtHeader(models.Model):
    emp_no = models.CharField(max_length=25)
    open_begin_dt = models.DateTimeField(blank=True, null=True)
    open_hse_dt = models.DateTimeField(blank=True, null=True)
    mod_hse_sts = models.CharField(max_length=1, blank=True, null=True)
    open_cp_dt = models.DateTimeField(blank=True, null=True)
    mod_cp_sts = models.CharField(max_length=1, blank=True, null=True)
    open_hd_dt = models.DateTimeField(blank=True, null=True)
    mod_hd_sts = models.CharField(max_length=1, blank=True, null=True)
    open_hr_dt = models.DateTimeField(blank=True, null=True)
    mod_hr_sts = models.CharField(max_length=1, blank=True, null=True)
    open_com_dt = models.DateTimeField(blank=True, null=True)
    mod_com_sts = models.CharField(max_length=1, blank=True, null=True)
    open_pt_dt = models.DateTimeField(blank=True, null=True)
    mod_pt_sts = models.CharField(max_length=1, blank=True, null=True)
    all_sts = models.CharField(max_length=1, blank=True, null=True)
    test_begin = models.DateTimeField(blank=True, null=True)
    test_sts = models.CharField(max_length=1, blank=True, null=True)
    key_token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cbt_header'


class TPostTest(models.Model):
    module = models.CharField(max_length=25, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    opt1 = models.TextField(blank=True, null=True)
    opt2 = models.TextField(blank=True, null=True)
    opt3 = models.TextField(blank=True, null=True)
    opt4 = models.TextField(blank=True, null=True)
    ans_valid = models.IntegerField(blank=True, null=True)
    sts_quiz = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post_test'


class TPostTestEmp(models.Model):
    emp_no = models.CharField(primary_key=True, max_length=30)
    id = models.IntegerField()
    module = models.CharField(max_length=30, blank=True, null=True)
    ans_value = models.IntegerField(blank=True, null=True)
    ans_valid = models.IntegerField(blank=True, null=True)
    sts_valid = models.CharField(max_length=1, blank=True, null=True)
    crt_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post_test_emp'
        unique_together = (('emp_no', 'id'),)


class Tempsending(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    doc_id = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempsending'


class Timeattendance(models.Model):
    yyyymm = models.CharField(primary_key=True, max_length=6)
    emp_no = models.CharField(max_length=18)
    wk_day = models.CharField(max_length=8)
    arriv_time = models.TimeField(blank=True, null=True)
    out_time = models.TimeField(blank=True, null=True)
    plan_in = models.TimeField()
    plan_out = models.TimeField()
    wk_type = models.CharField(max_length=3)
    description = models.CharField(max_length=200)
    loss_time = models.IntegerField()
    in_ot = models.TimeField(blank=True, null=True)
    out_ot = models.TimeField(blank=True, null=True)
    real_ot = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desc_ot = models.CharField(db_column='Desc_ot', max_length=200, blank=True, null=True)  # Field name made lowercase.
    upd_dt = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=18, blank=True, null=True)
    ot_description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeattendance'
        unique_together = (('yyyymm', 'emp_no', 'wk_day'),)


class Trainingrecord(models.Model):
    provider_id = models.IntegerField(blank=True, null=True)
    training_type = models.IntegerField(blank=True, null=True)
    training_category = models.IntegerField(blank=True, null=True)
    participant_category = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    emp_no = models.CharField(max_length=255, blank=True, null=True)
    start_dt = models.DateField(blank=True, null=True)
    finish_dt = models.DateField(blank=True, null=True)
    hours = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vanue = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainingrecord'


class Useraccount(models.Model):
    id_acc = models.AutoField(primary_key=True)
    user_acc = models.CharField(max_length=20)
    pass_acc = models.CharField(max_length=32)
    upd_pwd = models.DateField(blank=True, null=True)
    mail_acc = models.CharField(max_length=50, blank=True, null=True)
    img_acc = models.CharField(max_length=255, blank=True, null=True)
    upd_date = models.DateField(blank=True, null=True)
    sms_notification = models.CharField(max_length=3, blank=True, null=True)
    mobile_num = models.CharField(max_length=15, blank=True, null=True)
    emp_no = models.CharField(max_length=15, blank=True, null=True)
    ga_sts = models.CharField(max_length=10, blank=True, null=True)
    level_menus = models.IntegerField(blank=True, null=True)
    token_release = models.CharField(max_length=255, blank=True, null=True)
    token_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useraccount'


class Userlevelpermissions(models.Model):
    userlevelid = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=255)
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userlevelpermissions'
        unique_together = (('userlevelid', 'tablename'),)


class Userlevels(models.Model):
    userlevelid = models.IntegerField(primary_key=True)
    userlevelname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'userlevels'


class Vanotification(models.Model):
    period = models.CharField(primary_key=True, max_length=6)
    emp_no = models.CharField(max_length=15)
    wk_day = models.CharField(max_length=8)
    wk_type = models.CharField(max_length=3, blank=True, null=True)
    sts_send = models.CharField(max_length=3, blank=True, null=True)
    senddate = models.DateField(blank=True, null=True)
    mail_add = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'vanotification'
        unique_together = (('period', 'emp_no', 'wk_day'),)


class Workingcalendar(models.Model):
    wk_day = models.CharField(primary_key=True, max_length=8)
    wk_type = models.CharField(max_length=1, blank=True, null=True)
    wk_desc = models.CharField(max_length=255, blank=True, null=True)
    arriv_time = models.TimeField()
    out_time = models.TimeField()
    group_id = models.CharField(max_length=4)
    dy_name = models.CharField(max_length=3)
    yyyy = models.CharField(max_length=4)
    crt_dt = models.DateTimeField()
    upd_dt = models.DateTimeField()
    user_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'workingcalendar'
        unique_together = (('wk_day', 'group_id'),)
