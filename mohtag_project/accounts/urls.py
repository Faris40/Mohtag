from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('register/user/',views.user_register,name='user_register'),
    path('login/user/',views.user_login,name='user_login'),
    path('register/',views.charity_register,name='charity_register'),
    path('login/',views.charity_login,name='charity_login'),
    path('logout/',views.user_logout, name='user_logout')
]