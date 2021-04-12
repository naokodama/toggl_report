from django.urls import path

from . import views

app_name = 'toggl_report_app'
urlpatterns = [
    path('', views.UserView.as_view(), name='user_view'),
    ]

