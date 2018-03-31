from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin
from . import views

from accounts.forms import UserRegistrationForm
from registration.backends.default.views import RegistrationView
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = UserRegistrationForm), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^submission/', include('submission.urls', namespace='submission')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
