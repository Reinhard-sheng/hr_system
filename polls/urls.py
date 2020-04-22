from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login_fail/<str:name>', views.login_fail, name='login fail'),
    path('interviewer/<int:uid>', views.interviewer, name='interviewer'),
    path('login', views.login, name='login'),
]
