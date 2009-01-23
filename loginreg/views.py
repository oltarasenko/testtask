# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponse

def logout_page(request):
    logout(request)
    return HttpResponse("You're logged out")

def start_page(request):
    return render_to_response('start_page.html', RequestContext(request))
