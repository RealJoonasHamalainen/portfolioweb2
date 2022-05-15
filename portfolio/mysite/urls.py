from django.conf.urls import include, url
from mysite import views

urlpatterns = [
    url('', views.mysite, name='mysite'),
    
]