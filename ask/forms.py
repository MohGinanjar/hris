from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import Profile, FamilyMember
from api.models import MasterDivision

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields['div'] = forms.ModelChoiceField(queryset=MasterDivision.objects.all())
    class Meta:
        model = Profile
        exclude = ()
    
        


class FamilyMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['readonly'] = True
    class Meta:
        model = FamilyMember
        exclude = ('nik_emp','created_date')
    
        widgets = {
            'age': forms.TextInput(attrs={'class': 'date-picker form-control'}),
            'no_ktp': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            }


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=6)
