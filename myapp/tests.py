from django.test import TestCase
import datetime
from django.utils import timezone
from . import models

class Iso8601Tests(TestCase):
    """
    Test the use of datetime URL query values as ISO 8601 with timezones.
    """
    @classmethod
    def setUpTestData(cls):
        models.DateTimeModel.objects.create()
        cls.timestamp = timezone.now()
        models.DateTimeModel.objects.create()
        models.DateTimeModel.objects.create()

    def test_utc_lt(self):
        response = self.client.get('/testurl/?created__lt={}'.format(
            self.timestamp.isoformat(),
        ))
        self.assertEqual(len(response.json()), 1)

    def test_utc_gt(self):
        response = self.client.get('/testurl/?created__gt={}'.format(
            self.timestamp.isoformat(),
        ))
        self.assertEqual(len(response.json()), 2)

    def test_utc_minus_3h_lt(self):
        tz = datetime.timezone(datetime.timedelta(hours=-3))
        response = self.client.get('/testurl/?created__lt={}'.format(
            timezone.localtime(self.timestamp, tz).isoformat(),
        ))
        self.assertEqual(len(response.json()), 1)

    def test_utc_minus_3h_gt(self):
        tz = datetime.timezone(datetime.timedelta(hours=-3))
        response = self.client.get('/testurl/?created__gt={}'.format(
            timezone.localtime(self.timestamp, tz).isoformat(),
        ))
        self.assertEqual(len(response.json()), 2)

    def test_utc_plus_3h_lt(self):
        tz = datetime.timezone(datetime.timedelta(hours=+3))
        response = self.client.get('/testurl/?created__lt={}'.format(
            timezone.localtime(self.timestamp, tz).isoformat(),
        ))
        self.assertEqual(len(response.json()), 1)

    def test_utc_plus_3h_gt(self):
        tz = datetime.timezone(datetime.timedelta(hours=+3))
        response = self.client.get('/testurl/?created__gt={}'.format(
            timezone.localtime(self.timestamp, tz).isoformat(),
        ))
        self.assertEqual(len(response.json()), 2)

