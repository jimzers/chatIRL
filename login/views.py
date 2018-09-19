from django.views.generic import FormView
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

"""
class NewUserProfileView(FormView):
    template_name = "signup.html"
    form_class = ProfileForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("some url name")

"""
class SignUp(generic.CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.

# @login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
