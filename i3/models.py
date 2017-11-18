# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ship(models.Model):

    planet = models.IntegerField(default=0)
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
    ftl_on = models.BooleanField(default=True)

    def update(self):
        self.oxygen -= self.multiplier
        self.fuel -= self.multiplier
        if self.cooling:
            self.heat -= self.multiplier
        else:
            self.heat += self.multiplier

    def switch_cooling(self):
        self.cooling = not self.cooling
