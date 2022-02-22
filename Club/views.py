from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def meeting(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'Club/meeting.html', {'meeting_list': meeting_list})

def meetingDetail(request, id):
    meeting = get_object_or_404(Meeting, pk = id)
    return render(request, 'Club/meetingdetail.html', {'meeting': meeting})