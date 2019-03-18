
from django.test import TestCase
from .models import Meeting, Resource
from django.urls import reverse

# Create your tests here.
# model tests

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='raise payment')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='Laptop')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        minutes=MeetingMinutes(Minutestext='More Test')
        self.assertEqual(str(minutes), minutes.minutestext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'MeetingMinutes')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventitle='raise payment')
        self.assertEqual(str(event), event.eventitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')






