# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView


from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'i3/index.html'
    return render(request,template)


def wc(request):
    template = 'i3/wc.html'
    return render(request,template)


def cockpit(request):
    template = 'i3/cockpit.html'
    return render(request,template)


def engine(request):
    template = 'i3/engine.html'
    return render(request,template)