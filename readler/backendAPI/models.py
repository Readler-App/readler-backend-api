from django.db import models
from django.contrib.postgres.fields import ArrayField
from cuser.models import AbstractCUser


# Abstraction layer on top of CUser
class CustomUser(AbstractCUser):
    middleNames = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default="")


class Library(models.Model):
    name = models.CharField(max_length=30)
