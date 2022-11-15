from django.urls import path
from . import views

app_name = 'mohtag_app'


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('family_add/',views.new_family,name='new_family'),
    path('fa/',views.family,name='family'),
    path('don/',views.don,name='don')
    
]