from django.contrib import admin

# Register your models here.
from applications.dashboard.models import SocialMediaAccessToken

admin.site.register(SocialMediaAccessToken)
