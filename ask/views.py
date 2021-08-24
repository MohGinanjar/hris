from django.db import transaction, IntegrityError
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import render, redirect
from .forms import FamilyMemberFormSet
from .models import Profile, FamilyMember
from django.forms import modelformset_factory

class ProfileList(ListView):
    model = Profile


def listmemberfamily(request):
    data = FamilyMember.objects.all()
    context = {
        'data' : data,
    }
    return render(request, 'poll/profile_list.html')

class ListMemberFamily(ListView):
    model = Profile
    fields = ['name', 'div']
    success_url = reverse_lazy('poll:profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return data

class ProfileCreate(CreateView):
    model = Profile
    fields = ['name', 'div']


class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['nik','name','no_ktp','div','ask_1','ask_2','ask_3','ask_4']
    success_url = reverse_lazy('ask:profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        print(data)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()
            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['name', 'div']


class ProfileFamilyMemberUpdate(UpdateView):
    model = Profile
    fields = ['name', 'div']
    success_url = reverse_lazy('ask:profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST, instance=self.object)
        else:
            data['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')




# Create your views here.

# def create(request):
#     context = {}
#     MarksFormset = modelformset_factory(FamilyMember, form=MarksForm ,extra=6)	
#     form = StudentForm(request.POST or None)
#     formset = MarksFormset(request.POST or None, queryset= FamilyMember.objects.none(), prefix='marks')
#     if request.method == "POST":
#         if form.is_valid() and formset.is_valid():
#             try:
#                 with transaction.atomic():
#                     student = form.save(commit=False)
#                     student.save()
                        
#                     for mark in formset:
#                         data = mark.save(commit=False)
#                         data.student = studentprint(data)
#                         print(data)
#                         data.save()
#             except IntegrityError:
#                 print("Error Encountered")

#             return redirect('poll:list')


#     context['formset'] = formset
#     context['form'] = form
#     return render(request, 'poll/create.html', context)

# def create(request):
#     context={}
#     MarksFormset = modelformset_factory(FamilyMember, form=MarksForm ,extra=6)
#     form = StudentForm(request.POST or None)
#     formset = MarksFormset(request.POST or None, queryset= FamilyMember.objects.none(), prefix='marks')
#     if request.method == "POST":
#         if form.is_valid() and formset.is_valid():
#             try:
#                 with transaction.atomic():
#                     student = form.save(commit=False)
#                     print(student)
#                     student.save()
#                     for mark in formset:
#                         data = mark.save(commit=False)
#                         print(data)
#                         data.profile = studentprint(data)
#                         data.save()
#             except IntegrityError:
#                 print("Error Encountered")
#                 return redirect('poll:list')
#     context['formset'] = formset
#     context['form'] = form
#     return render(request, 'poll/create.html', context)
            



# def list(request):
# 	datas = Student.objects.all()
# 	return render(request, 'poll/list.html', {'datas':datas})