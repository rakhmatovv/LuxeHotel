from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('servies/', views.services, name='services'),
    path('room_list/<slug:slug>/', views.RoomListView, name='room_category'),
    path('room/<slug:slug>', views.room_detail, name='room_detail')
]
