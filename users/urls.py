from django.urls import path
from . import views



urlpatterns = [
    path('',views.home_page,name='home'),
    path('loign/',views.login_page,name='login'),
    path('register/',views.sign_up_page,name='register'),
    path('logout/',views.Logout_page,name='logout'),   
    path('create_post/',views.create_post,name='create_post'),
    path('createpage/',views.createpage,name='createpage'),    
]
