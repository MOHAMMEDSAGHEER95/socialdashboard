from rest_framework import serializers

from applications.dashboard.models import SocialMediaAccessToken


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(allow_blank=False, trim_whitespace=True,)


class UpdatePageInfoSerializer(serializers.Serializer):
    about = serializers.CharField(required=False, allow_blank=True)
    emails = serializers.EmailField(required=False)
    website = serializers.URLField(required=False, allow_blank=True)
    phone = serializers.IntegerField(required=False)

    def to_internal_value(self, data):
        formatted_data = {k: v for k, v in data.items() if v}
        if 'emails' in formatted_data:
            formatted_data['emails'] = [formatted_data['emails']]  # emails should be sent as array to facebook
        return formatted_data
