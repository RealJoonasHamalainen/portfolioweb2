from django.conf import settings
from django.views import *
from django.contrib import admin
from django.conf.urls import  include, url
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url("", include("mysite.urls")),
    url('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

