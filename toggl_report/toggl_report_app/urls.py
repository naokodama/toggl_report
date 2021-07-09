from django.urls import path

from . import views

app_name = 'toggl_report_app'
urlpatterns = [
    path('', views.UserView.as_view(), name='user_view'),
    path('<str:pk>/daily_report/', views.DailyView.as_view(), name='daily_report'),
    path('<str:user_id>/daily_report/<str:date>/', views.daily_view, name='daily_report_view'),
    path('<str:user_id>/daily_report/<str:date>/circle_graph', views.showCircleGraph, name='show_circle_graph'),
    ]

