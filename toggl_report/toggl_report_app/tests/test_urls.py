# [ ] 対象者を選択するための画面を作成する
# [ ] 対象者を登録するための画面を作成する
# [ ] 対象者を選択した後の画面を作成する
# [ ] 複数人のtogglのデータのグラフを比較できるような画面を作成する
# [ ] 

from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from .. import views 

class TopPageTest(TestCase):
    def test_post_top_page(self):
        url = reverse("toggl_report_app:user_view")
        self.assertEqual(resolve(url).func.view_class, views.UserView)

class UserFormTest(TestCase):
    def test_post_user_form_page(self):
        view = reverse("user_regist/")
        self.assertEqual(views.UserRegist.as_view(), user_regist_view)

class TimeLineTest(TestCase):
    def test_post_timeline_view(self):
        view = reverse("timeline/")
        self.assertEqual(views.TimelineView.as_view(), timeline_view)

class CircleViewTest(TestCase):
    current_date = "{0:%Y-%m-%d}".format(timezone.now())
    def test_post_circleview_test(self):
        view = reverse("toggl_report_app:circle_view")
        self.assertEqual(views.CircleView.as_view(), circle_view)

class StickViewTest(TestCase):
    def test_post_stickview_test(self):
        view = reverse("stick_view/")
        self.assertEqual(views.StickView.as_view(), stick_view)
