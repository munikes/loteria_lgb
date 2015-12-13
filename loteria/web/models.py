from __future__ import unicode_literals

from django.db import models

class LotteryUser(models.Model):
    name = models.CharField(max_length=200)
    number = models.DecimalField(max_digits=5, decimal_places=0)
    prize = models.IntegerField(default=0)

