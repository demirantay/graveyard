from django.test import TestCase
from django.contrib.auth.models import User
from home_app.models import Office, OfficeWorkers, Announcament


# TESTING THE OFFICE MODEL
class TestOfficeModel(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        Office.objects.create(admin=user, name='test_office')

    def test_to_string(self):
        office = Office.objects.get(id=1)
        expected_to_string = "test_office"
        self.assertEqual(expected_to_string, str(office))


# TEST OFFICE WORKERS MODEL
class TestOfficeWorkersModel(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        office = Office.objects.create(admin=user, name='test_office')
        OfficeWorkers.objects.create(user=user, joined_office=office)

    def test_to_string(self):
        office_worker = OfficeWorkers.objects.get(id=1)
        expected_to_string = 'test_user'
        self.assertEqual(expected_to_string, str(office_worker))


# TEST ANNOUNCAMENT MODEL
class TestAnnouncamentModel(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        announcament = Announcament.objects.create(user=user, content='test')

    def test_to_string(self):
        announcament = Announcament.objects.get(id=1)
        expected_to_string = "test_user"
        self.assertEqual(expected_to_string, str(announcament))
