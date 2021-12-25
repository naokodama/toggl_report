from django.test import TestCase
from django.urls import reverse

class TopPageTest(TestCase):
    def test_port_top_page(self):
        view = reverse("/")
        self.assertEqual(views.UserView.as_view(), user_view)

class UserFormTest(TestCase):
    def test_post_user_form_page(self):
        view = reverse("user_regist/")
        self.assertEqual(views.UserRegist.as_view(), user_regist_view)

class TimeLineTest(TestCase):
    def test_port_timeline_view(self):
        view = reverse("timeline/")
        self.assertEqual(views.TimelineView.as_view(), timeline_view)

class CircleViewTest(TestCase):
    def test_post_circleview_test(self):
        view = reverse("circle_view/")
        self.assertEqual(views.CircleView.as_view(), circle_view)

class StickViewTest(TestCase):
    def test_post_stickview_test(self):
        view = reverse("stick_view/")
        self.assertEqual(views.StickView.as_view(), stick_view)
