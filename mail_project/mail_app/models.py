from django.db import models
from django.utils import timezone
import datetime
import os

# Create your models here.

class IncomingFiles(models.Model):
    incoming_file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=200)
    date_received = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=64)
    protocol = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
    last_touched = models.CharField(max_length=64)
    file= models.FileField(upload_to='.')

    def __str__(self):
        return self.file_name

'''
class OutgoingGroup(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=200)
    partner_name = models.CharField(max_length=200)
    status = models.CharField(max_length=64)
    protocol = models.CharField(max_length=50)
    sitename = models.CharField(max_length=200)
    owner = models.CharField(max_length=64)
    last_touched = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.file_id}, {self.file_name}"
'''

