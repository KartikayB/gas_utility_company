from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class User_info(models.Model):
    STATUS = [
        ("ACK", "ACCEPTED"),
        ("REJ", "REJECTED"),
        ("INP", "IN PROGRESS"),
        ("COM", "COMPLETED")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.AutoField(primary_key=True)
    issue = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    extra_info = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS,
        default='ACK',max_length=3)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True)
    admin_note = models.CharField(max_length=255, blank=True)
