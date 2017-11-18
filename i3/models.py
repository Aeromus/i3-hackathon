# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random

Planets = ["648721","876194","846721","427619","465973","321678","976382","346197","276481","000000"]

# Create your models here.

class Ship(models.Model):

    planet = models.IntegerField(default=0)
    distance_to_planet = models.FloatField(default=10000)
    health = models.FloatField(default=1000)
    multiplier = models.FloatField(default=0.001)
    oxygen = models.FloatField(default=100)
    heat = models.FloatField(default=50)
    cooling = models.BooleanField(default=True)
    fuel = models.FloatField(default=100)
    current_shield = models.CharField(max_length=4,default='aaaa')
    ideal_shield = models.CharField(max_length=4,default='aaaa')
    gps = models.CharField(max_length=6, default='000000')
    self_destruct = models.BooleanField(default=False)
    ftl_on = models.BooleanField(default=False)

    def update(self):
        self.oxygen -= self.multiplier
        self.fuel -= self.multiplier
        if self.cooling:
            self.heat -= self.multiplier
        else:
            self.heat += self.multiplier
        if self.distance_to_planet < 1:
            self.planet += 1
            self.distance_to_planet = 10000
            self.multiplier *= 10
        if self.ftl_on:
            if self.gps == Planets[self.planet]:
                self.distance_to_planet -= 10 + random.randint(1,100)
            else:
                self.distance_to_planet += random.randint(-20,20)

    def switch_cooling(self):
        self.cooling = not self.cooling
