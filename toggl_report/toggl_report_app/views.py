from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse(template.render(context, request))
    return render(request, 'toggl_report_app/index.html', '')
    # return HttpResponse("test")
