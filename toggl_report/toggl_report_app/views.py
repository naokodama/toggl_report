from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.views import generic

from .models import TogglUser

class UserView(generic.ListView):
    template_name = 'toggl_report_app/index.html'
    context_object_name = 'user_select'

    def get_queryset(self):
        return TogglUser.objects.order_by('user_id')

class DailyView(generic.DetailView):
    template_name = 'toggl_report_app/daily_report.html'
    model = TogglUser
    context_object_name = 'toggl_user'

    def get_queryset(self):
        return TogglUser.objects.order_by('user_id')
