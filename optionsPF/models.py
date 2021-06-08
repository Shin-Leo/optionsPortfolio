from django.contrib.postgres.fields import ArrayField
from django.db import models


class Dates(models.Model):
    date = ArrayField(
        models.CharField(max_length=14, editable=True), size=30
    )