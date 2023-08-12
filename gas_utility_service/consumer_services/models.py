from django.db import models
import datetime
from django.contrib.auth.models import User


class User_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.AutoField(primary_key=True)
    issue = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    extra_info = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default='accepted')
    date_updated = models.DateTimeField(default=datetime.datetime.now)
    file = models.FileField()
