from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.User_register, name='register'),
    path('login/',views.User_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/pass_change_with_pass',views.PassWord_change, name='PassWord_change_with_pass'),
    path('profile/pass_change_without_pass',views.PassWord_change2, name='PassWord_change'),
]