import datetime as dt

from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.db.models.manager import Manager


class BaseModel(models.Model):
    created_at: dt.datetime = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at: dt.datetime = models.DateTimeField(editable=False, null=True, blank=True)
    objects = Manager()

    class Meta:
        abstract = True
        indexes = (BrinIndex(fields=("created_at", "updated_at")),)
