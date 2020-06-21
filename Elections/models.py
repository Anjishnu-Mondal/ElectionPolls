from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# class VoterInfo(models.Model):
#     voterCardNo = models.CharField(
#         max_length = 30,
#         primary_key = True)
#     aadharCardNo = models.IntegerField(
#         max_length = 12,
#         unique = True)
#     state = models.CharField(
#         max_length = 25
#         )

#     def __str__(self):
#         return self.name

    # class Meta:
    #     db_table = "VoterInfo"

# class PartyInfo(models.Model):
#     partyName = models.CharField(
#         max_length = 30,
#         required = True
#     )
#     voteCount = models.IntegerField(
#         default = 0
#     )

#     class Meta:
#         db_table = "PartyInfo"