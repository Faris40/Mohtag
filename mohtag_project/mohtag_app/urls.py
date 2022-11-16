from django.urls import path
from . import views

app_name = 'mohtag_app'


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('family_add/',views.new_family,name='new_family'),
    path('fa/',views.family,name='family'),
    path('don/',views.don,name='don'),
    path('don/view/',views.view_don,name='view_don'),
    path('don/del/<donation_id>/',views.del_don, name= 'donation_del'),
    path('family/del/<family_id>/',views.del_family, name= 'family_del'),
    path('home/no_perm/', views.no_perm, name='no_perm')
    
]