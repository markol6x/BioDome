from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Let us add some simple fields to profile
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    given_name = models.CharField(max_length=50, default='')
    middle_name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    institution = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return u"%s" % self.user

from registration.signals import user_registered
def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.given_name = request.POST["given_name"]
    profile.middle_name = request.POST["middle_name"]
    profile.surname = request.POST["surname"]
    profile.institution = request.POST["institution"]
    profile.save()

user_registered.connect(user_registered_callback)
