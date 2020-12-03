from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class Tracker(models.Model):

    """
    Base model for Postgresql DB.
    """

    created = CreationDateTimeField(_('Created at'))
    modified = ModificationDateTimeField(_('Modified at'))

    class Meta:
        abstract = True


class SocialMediaAccessToken(Tracker):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media_handle')
    page_id = models.CharField(max_length=250, null=True, blank=True)
    user_access_token = models.TextField(max_length=250,help_text=("facebook user access token(no expiry)"),
                                         null=True, blank=True)

    class Meta:
        verbose_name = _('Social Media Token')
        verbose_name_plural = _('Social Media Tokens')

    def __str__(self):
        return self.name
