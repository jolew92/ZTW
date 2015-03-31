from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.template import RequestContext


def user_name(request):
    return render_to_response('base.html', {'user': request.user}, context_instance=RequestContext(request))


def home(request):
    return render_to_response("index.html")