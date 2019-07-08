from django.test import TestCase
from myweb.models import Event,Guest

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address='shenzhen',start_time='2019-07-01 10:00:00')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='12345678908')