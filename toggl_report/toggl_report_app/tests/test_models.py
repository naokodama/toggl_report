from django.test import TestCase
from toggl_report_app.models import TogglUser
from toggl_report_app.models import SelectedUser

class SelectedUserTest(TestCase):
    def test_not_exist_selected_user(self):
        selected_user = SelectedUser.objects.all()
        self.assertEqual(selected_user.count(), 0)
