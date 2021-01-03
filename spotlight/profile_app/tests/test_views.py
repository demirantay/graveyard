from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home_app.models import Office
import unittest


# TESTING PROFILE SETTINGS VIEW
class TestProfileSettingsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test_user', password='123')
        self.office = Office.objects.create(name='foo', admin=self.user)

    def test_view_is_accesible_by_name(self):
        office = Office.objects.get(id=1)
        response = self.client.get(reverse('settings', args=[office.name]))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_uses_correct_template(self):
        office = Office.objects.get(id=1)
        login = self.client.login(username='test_user', password='123')
        response = self.client.get(reverse('dashboard', args=[office.name]))
        # Check User is logged in
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('settings.html')
