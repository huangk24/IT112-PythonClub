from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
]