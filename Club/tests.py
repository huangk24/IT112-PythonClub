from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingtitle = 'New Year')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'New Year')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class EventTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingtitle = 'New Year')
        self.user = User(username = 'user1')
        self.event = Event(eventtitle = 'New Year', location = 'Seattle', 
                           date = datetime.date(2022, 3, 1), description = 'Celebrate Chinese New Year')

    def test_string(self):
        self.assertEqual(str(self.event), 'New Year')

    def test_location(self):
        self.assertEqual(str(self.event.location), 'Seattle')

class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(resoucename = 'Dumplings')
        self.user = User(username = 'user1')
        self.resource = Resource(resoucetype = 'Food', description = 'A traditional chinese food')

    def test_string(self):
        self.assertEqual(str(self.resource), 'Dumplings')

class newMeetingForm(TestCase):
    def test_meetingForm(self):
        data={
             'meetingtitle': 'Pi Day', 
             'meetingdate': '2022-03-14', 
             'location': 'Seattle Central',
             'agenda': 'Celebrate Pi Day!'
        }
        form = MeetingForm(data)
        self.assertTrue(form.is_valid)

class New_Meeting_Authetication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objecrs.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Type.objects.create(typename='Spring break')
        self.event=event.objects.create(eventtitle = 'Spring break', location = 'Seattle', 
                           date = datetime.date(2022, 3, 15), description = 'Spring break')

    def test_redirect_if_not_logged_in(self):
        response.self.client.get(reverse('newproduct'))
        self.assertRediects(response, '/accounts/login/?next=/Club/newmeeting/')