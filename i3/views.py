# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView

from models import Ship
from django.shortcuts import render

Current_Ship = 8

# Create your views here.
def index(request):
    template = 'i3/index.html'
    return render(request,template)


def wc(request):
    template = 'i3/wc.html'
    return render(request,template)


def cockpit(request):
    template = 'i3/cockpit.html'
    ship, created = Ship.objects.get_or_create(pk=Current_Ship)
    return render(request,template,{'Ship': ship})


def engine(request):
    template = 'i3/engine.html'
    ship, created = Ship.objects.get_or_create(pk=Current_Ship)
    return render(request,template,{'Ship': ship})


def status(request):
    ship, created = Ship.objects.get_or_create(pk= Current_Ship)
    ship.update()
    shield = not (ship.current_shield + 10 > ship.ideal_shield and ship.current_shield - 10 < ship.ideal_shield)
    ship.save()
    template = 'i3/status.html'
    return render(request,template,{'Ship': ship,'Shield':shield})


def cooling_switch(request):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.switch_cooling()
    ship.save()
    return HttpResponse(str(ship.cooling))


def set_gps(request,gps_coords):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.gps = gps_coords
    ship.save()
    return HttpResponse('BUENO')


def itinerary(request):
    template = 'i3/itinerary.html'
    return render(request,template)


def ftl_on(request):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.ftl_on = True
    ship.save()
    return HttpResponse('BUENO')


def pump_oxygen(request):
    ship = Ship.objects.get(pk=Current_Ship)
    if ship.oxygen < 150:
        ship.oxygen += 1
    ship.save()
    return HttpResponse('BUENO')


def move_fuel(request):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.engine_fuel += 1
    ship.save()
    return HttpResponse('BUENO')


def enter_fuel(request):
    ship = Ship.objects.get(pk=Current_Ship)
    if ship.engine_fuel > 0:
        ship.engine_fuel -= 1
        ship.fuel += 1
    ship.save()
    return HttpResponse('BUENO')


def set_shield(request,shield_val):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.current_shield = shield_val
    ship.save()
    return HttpResponse('BUENO')