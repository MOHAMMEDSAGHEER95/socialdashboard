from rest_framework import serializers

from applications.dashboard.models import SocialMediaAccessToken


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(allow_blank=False, trim_whitespace=True,)


class UpdatePageInfoSerializer(serializers.Serializer):
    about = serializers.CharField(required=False)
    emails = serializers.ListField(child=serializers.EmailField())  # emails should be sent as array to facebook
    website = serializers.URLField(required=False)
    phone = serializers.IntegerField(required=False)
