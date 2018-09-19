from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

# max_length=50, blank=True,
# null=True, blank=True,
# blank=True,
'''
class UserCreateForm(UserCreationForm):
    location = forms.CharField(max_length=50)
    birth_date = forms.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    class Meta:
        model = User

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Profile(user=user, location=self.cleaned_data['location'],
                               birth_date=self.cleaned_data['birth_date'], phone_number=self.cleaned_data['phone_number'])
        user_profile.save()
        return user, user_profile
'''

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'location', 'birth_date', 'phone_number')

    def save(self, user=None):
        user_profile = super(ProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
            user_profile.save()
            return user_profile

