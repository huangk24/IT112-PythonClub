from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def meeting(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'Club/meeting.html', {'meeting_list': meeting_list})