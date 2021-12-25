from django.test import TestCase
from toggl_report_app.models import TogglUser
from toggl_report_app.models import SelectedUser

class TogglUserTests(TestCase):

class SelectedUserTest(TestCase):
    def test_not_exist_selected_user():
        selected_user = SelectedUser.object.all()
        self.assertEqual(select_user.count(). 0)
