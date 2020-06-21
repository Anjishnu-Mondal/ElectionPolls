from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class PartyInfo(models.Model):
    partyName = models.CharField(
        max_length = 30,
        required = True
    )
    voteCount = models.IntegerField(
        default = 0
    )

    class Meta:
        db_table = "PartyInfo"