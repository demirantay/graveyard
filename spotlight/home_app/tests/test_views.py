from django.test import TestCase, Client
from django.urls import reverse
import unittest
from django.contrib.auth.models import User
from home_app.models import Office, OfficeWorkers, Announcament


# TESTING THE HOME VIEW
class TestHomeView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')


# TESTING THE SIGNUP VIEW
class TestSignupView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        response = self.client.get("/home/signup/")
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('signup.html')


# TESTING THE LOGIN VIEW
class TestLoginView(TestCase):

    def setUp(self):
        pass

    def test_view_exists_at_desired_url(self):
        response = self.client.get("/home/login/")
        self.assertEqual(response.status_code, 200)

    def test_view_is_accesible_by_name(self):
        response = self.client.get(reverse('login_gate'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login_gate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login_gate.html')


# TESTING OFFICE DASHBOARD
class TestDashboardView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test_user', password='123')
        self.office = Office.objects.create(name='foo', admin=self.user)

    def test_view_is_accesible_by_name(self):
        office = Office.objects.get(id=1)
        response = self.client.get(reverse('dashboard', args=[office.name]))
        self.assertEqual(response.status_code, 302)

    def test_view_works_with_args(self):
        office = Office.objects.get(id=1)
        response = self.client.get(reverse('dashboard', args=[office.name]))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_uses_correct_template(self):
        office = Office.objects.get(id=1)
        login = self.client.login(username='test_user', password='123')
        response = self.client.get(reverse('dashboard', args=[office.name]))
        # Check User is logged in
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('dashboard.html')


# TESTING DESK BROWSE VIEW
class TestDeskBrowseView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test_user', password='123')
        self.office = Office.objects.create(name='foo', admin=self.user)

    def test_view_is_accesible_by_name(self):
        office = Office.objects.get(id=1)
        response = self.client.get(reverse('desk_browse', args=[office.name]))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_uses_correct_template(self):
        office = Office.objects.get(id=1)
        login = self.client.login(username='test_user', password='123')
        response = self.client.get(reverse('desk_browse', args=[office.name]))
        # Check User is logged in
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('desk_browse.html')
