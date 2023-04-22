# Created by the admin

from django.contrib import admin
from django.urls import path,include
from home  import views

# test user passwords
# hriday ---> pass hraj@420

urlpatterns = [
    path('', views.index, name='home'),
    path('live', views.live, name='live'),
    path('analyze',views.analyze, name='analyze'),

    
    
]