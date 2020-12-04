from django.contrib import admin

# Register your models here.
from applications.dashboard.models import SocialMediaAccessToken


class SocialMediaAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')


admin.site.register(SocialMediaAccessToken, SocialMediaAccessTokenAdmin)
