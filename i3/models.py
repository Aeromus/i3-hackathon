# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ship(models.Model):

    oxygen = models.IntegerField(default=100)
    heat = models.IntegerField(default=50)
    cooling = models.BooleanField(default=True)
    fuel = models.IntegerField(default=100)
    current_shield = models.CharField(max_length=4,default='aaaa')
    ideal_shield = models.CharField(max_length=4,default='aaaa')
    gps = models.CharField(max_length=6, default='000000')
    self_destruct = models.BooleanField(default=False)
    ftl_on = models.BooleanField(default=True)