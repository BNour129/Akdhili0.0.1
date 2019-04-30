from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileDetail(admin.ModelAdmin):
    list_display = ['user', 'Name', 'lastname', 'account_type']

admin.site.register(Profile, ProfileDetail)
