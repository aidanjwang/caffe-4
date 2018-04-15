from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
