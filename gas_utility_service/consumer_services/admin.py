from django.contrib import admin
from .models import User_info
# Register your models here.

class UserComplaintDisplay(admin.ModelAdmin):
  list_display = ("issue_id", "user", "issue", "status", "date_created", "updated_at", "admin_note")


admin.site.register(User_info, UserComplaintDisplay)
