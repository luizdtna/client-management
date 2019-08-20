from django.contrib import admin
from django.urls import path
from .views import home, my_logout


urlpatterns = [
    path('', home, name='url_home' ),
    path('logout/', my_logout, name ='logout'),
]