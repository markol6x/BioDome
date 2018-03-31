from django.conf.urls import url
from .views import EditUserProfileView

app_name = 'accounts'
urlpatterns = [
    url(r'^update_profile/(?P<pk>\d+)/', EditUserProfileView.as_view(), name='update_profile')
]
