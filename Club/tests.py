from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

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