from django.test import TestCase
from django.contrib.auth.models import User
from profile_app.models import ProfileSettings


# TESTING PROFILE SETTINGS MODEL
class TestingProfileSettingsModel(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='123')
        ProfileSettings.objects.create(user=user, bio='test_bio')

    def test_to_string(self):
        profile = ProfileSettings.objects.get(id=1)
        expected_to_str = "test_user"
        self.assertEqual(profile.user.username, expected_to_str)
