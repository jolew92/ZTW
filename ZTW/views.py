from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def home(request):
    return render(request, "index.html")