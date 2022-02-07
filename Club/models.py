from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length = 255)
    meetingdate = models.DateField(null = False, blank = False)
    meetingtime = models.TimeField(null = False, blank = False)
    location = models.CharField(max_length = 255)
    agenda = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendence = models.IntegerField()
    minutetext = models.TextField(null = True, blank = True)
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resoucename = models.CharField(max_length = 255)
    resoucetype = models.CharField(max_length = 255)
    url = models.URLField()
    dateentered = models.DateField(null = False, blank = False)
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.resoucename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(null = False, blank = False)
    description = models.TextField(null = True, blank = True)
    userid = models.IntegerField()

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
