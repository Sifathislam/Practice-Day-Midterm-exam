from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.AddMusician.as_view(),name='add_musician'),
    path('register/', views.SignUpViewClass.as_view(), name='register'),
    path('login/',views.UserLoginViewClass.as_view(), name = 'login'),
    path('logout/',views.UserLogoutViewClass.as_view(), name = 'logout'),
]
