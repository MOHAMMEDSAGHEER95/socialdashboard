from rest_framework import serializers

from applications.dashboard.models import SocialMediaAccessToken


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(allow_blank=False, trim_whitespace=True,)


class UpdatePageInfoSerializer(serializers.Serializer):
    about = serializers.CharField(required=False, allow_blank=True)
    emails = serializers.EmailField(required=False)  # emails should be sent as array to facebook
    website = serializers.URLField(required=False, allow_blank=True)
    phone = serializers.IntegerField(required=False)

    def to_internal_value(self, data):
        try:
            data['emails'] = [data['emails']] if data['emails'] else None
        except KeyError as e:
            pass
        formatted_data = {k: v for k, v in data.items() if v is not None}
        return formatted_data
