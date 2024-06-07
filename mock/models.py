from django.db import models


class MockModel(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100, unique=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    method = models.CharField(null=True, blank=True, max_length=10)
    path = models.CharField(null=True, blank=True, max_length=100, unique=True)
    res = models.JSONField(null=True, blank=True)



