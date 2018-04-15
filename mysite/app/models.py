from django.db import models


class MegaOrder(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    asin = models.CharField(max_length=100)
    description = models.CharField(default = "", max_length=2000)
    units = models.IntegerField(default=0)
    price = models.FloatField(default=0)


class MiniOrder(models.Model):
    order = models.ForeignKey(MegaOrder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    units = models.IntegerField(default=0)
