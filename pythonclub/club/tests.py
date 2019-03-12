
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
