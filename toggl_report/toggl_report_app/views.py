import requests
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

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
    today = "{0:%Y-%m-%d}".format(timezone.now())

    def render_to_response(self, context, **response_kwargs):
        return HttpResponseRedirect(reverse('toggl_report_app:daily_report_view', args = (context['toggl_user'].user_id, self.today, )))

    def get_queryset(self):
        return TogglUser.objects.filter()

def daily_view(request, user_id, date):
    user_info = get_object_or_404(TogglUser, pk = user_id)
    result = requests.get('https://www.toggl.com/api/v8/workspaces', auth = (user_info.api_token, 'api_token'))
    data = result.json()
    Data = data[0]
    context = {'workspace_id' : Data['id']}
    params = {
        'user_agent': user_info.mail,
        'workspace_id': Data['id'],
        'since': date,
        'until': date,
    }
    r = requests.get('https://toggl.com/reports/api/v2/details',
                     auth=HTTPBasicAuth(user_info.api_token, 'api_token'),
                     params=params)
    json_r = r.json()
    context = {'workspace_id' : Data['id'], 'report_json' : json_r}

    return render(request, 'toggl_report_app/daily_report.html', context)
