from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "accounts/update_user_form.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])

        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("home")
