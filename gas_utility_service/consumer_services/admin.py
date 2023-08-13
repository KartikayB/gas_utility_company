from django.contrib import admin
from .models import User_info
# Register your models here.

class UserComplaintDisplay(admin.ModelAdmin):
  list_display = ("user", "issue_id", "issue", "status", "date_updated")


admin.site.register(User_info, UserComplaintDisplay)
