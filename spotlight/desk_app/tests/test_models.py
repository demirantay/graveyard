from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office
from desk_app.models import Desk


class TestingDeskModel(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        office = Office.objects.create(admin=user, name='test_office')
        Desk.objects.create(sub_editor=user, office=office, name='test_name')

    def test_to_string(self):
        desk = Desk.objects.get(id=1)
        expected_to_str = 'test_name'
        self.assertEqual(expected_to_str, desk.name)
