from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class VoterInfo(models.Model):
    voterCardNo = models.CharField(max_length = 30)
    aadharCardNo = models.IntegerField(max_length = 12)
    state = models.CharField(max_length = 25)

    class Meta:
        db_table = "VoterInfo"