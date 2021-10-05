import requests
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

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
    context = {'workspace_id' : Data['id'], 'report_json' : json_r['data'], 'date': date, 'user_id': user_id}

    return render(request, 'toggl_report_app/daily_report.html', context)

def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    png_data = buf.getvalue()
    buf.close()
    return png_data

def getTogglData(user_id, date):
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
    return json_r['data']

def showCircleGraph(request, user_id, date):
    toggl_data = getTogglData(user_id, date)
    labels = []
    sizes = []
    for tdata in toggl_data:
        labels.append(tdata['description'])
        sizes.append(tdata['dur'])

    fig, ax = plt.subplots()
    patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                       shadow=True, startangle=90, labeldistance=0.7, pctdistance=0.5, wedgeprops={'linewidth': 1, 'edgecolor':"0.8"})
    ax.axis('equal') # 面積比=割合
    plt.rcParams['font.family'] = 'MS Gothic'
    plt.setp(autotexts, size=12)
    png_data = plt2png()
    plt.cla()
    response = HttpResponse(png_data, content_type='image/png')
    return response

