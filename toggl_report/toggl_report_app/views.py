from django.shortcuts import render

def index(request):

    return render(request, 'toggl_report_app/index.html', {})

