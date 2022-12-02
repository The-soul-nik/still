from django.urls import path, re_path
from . import views

app_name = 'akimov'

urlpatterns = [
	path('', views.home, name='home'),
	re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
	


]