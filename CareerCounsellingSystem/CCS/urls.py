
from django.urls import path,include
from . import views as ccs_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home',ccs_view.index,name='home'),
    path('',ccs_view.index),
    path('team',ccs_view.ourteam,name="team"),
    path('register/', ccs_view.register, name='register'),
    path('contact/',ccs_view.contact,name="contact"),
    path('login/', auth_views.LoginView.as_view(template_name='CCS/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='CCS/index.html'), name='logout'),
    path('accounts/profile/', ccs_view.userparameters, name='form'),

]