from . import views
from django.urls import path

urlpatterns = [


    
    path('login/', views.user_login, name='login'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('add_address/', views.add_address, name='add_address'),
    path('change_password/', views.change_password, name='change_password'),
    


]
