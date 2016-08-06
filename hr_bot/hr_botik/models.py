from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
import json

phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="not a phone number,it must look like +37477777777777, max 15 digits")


class HRQuery(models.Model):
#    def __init__(self, title, skills=None, age=None, location=None):
#        self.dreamtitle = models.CharField(max_length=150)
#        if skills:
#            self.dreamskills = models.CharField(max_length=150)
#        if age:
#            self.dreamage = models.DecimalField(max_digits=2, decimal_places=2)
#        if location:
#            self.dreamlocation = models.CharField(max_length=150)
    dreamtitle = models.CharField(max_length=150)
    dreamskills = models.CharField(max_length=150, blank=True)
    dreamage = models.FloatField(blank=True)
    dreamlocation = models.CharField(max_length=150, blank=True)

    def GetCandidate(self, number=1):
        if Candidate.objects.all().filter(age=dreamage).filter():
            return pass

    def MakeMatch():
        #to make matches for query-candidate
        pass

    def __str__(self):
        return self.dreamtitle


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(blank=True)
    gender = models.NullBooleanField()
    phone_number = models.Charfield(validators=[phone_validator], blank=True)
    title = models.CharField(max_length=150)
    skills = models.CharField(max_length=200)#to be edited, may be a json field with dumped list will do
    age = models.FloatField(blank=True)
    location = models.CharField(blank=True, max_length=50 )
    url = models.URLField()
