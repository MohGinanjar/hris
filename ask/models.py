from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone

VAKSIN_CHOICES = (
    ('ya','YA'),
    ('tidak', 'TIDAK'),
)

VAKSIN_CHOICES_K = (
    ('belum','BELUM'),
    ('sudah', 'SUDAH'),
)
class Profile(models.Model):
    nik = models.CharField(max_length=12,)
    name = models.CharField(max_length=100,)
    no_ktp = models.CharField(max_length=100,)
    div = models.CharField(max_length=100,)
    ask_1 = models.CharField(max_length=10,choices=VAKSIN_CHOICES_K, default='tidak')
    ask_2 = models.CharField(max_length=10,choices=VAKSIN_CHOICES_K, default='tidak')
    ask_3 = models.CharField(max_length=10,choices=VAKSIN_CHOICES, default='belum')
    ask_4 = models.CharField(max_length=10,choices=VAKSIN_CHOICES, default='belum')
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} {self.div}"
    

    


RELATIONS = (
    ('suami','SUAMI'),
    ('istri', 'ISTRI'),
    ('anak', 'ANAK'),
)

class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, related_name="marks", on_delete=models.CASCADE,blank=True, null=True)
    no_ktp = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    relationship = models.CharField(max_length=100,choices=RELATIONS, default='suami')
    age = models.CharField(max_length=100)
    ask_1 = models.CharField(max_length=10,choices=VAKSIN_CHOICES_K, default='tidak')
    ask_2 = models.CharField(max_length=10,choices=VAKSIN_CHOICES_K, default='tidak')
    ask_3 = models.CharField(max_length=10,choices=VAKSIN_CHOICES, default='belum')
    ask_4 = models.CharField(max_length=10,choices=VAKSIN_CHOICES, default='belum')
    nik_emp = models.CharField(max_length=12,blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
