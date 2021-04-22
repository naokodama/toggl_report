import requests
from django.shortcuts import render, get_object_or_404
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
        return TogglUser.objects.filter()

def daily_view(request, user_id):
    user_info = get_object_or_404(TogglUser, pk = user_id)
    result = requests.get('https://www.toggl.com/api/v8/workspaces', auth = (user_info.api_token, 'api_token'))
    data = result.json()
    Data = data[0]
    context = {'workspace_id' : Data['id']}
    return render(request, 'toggl_report_app/daily_report.html', context)
