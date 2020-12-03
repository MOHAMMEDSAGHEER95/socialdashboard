import requests
from django.conf import settings


def get_long_lived_user_token(short_lived_user_token):
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}' \
          '&client_secret={}&fb_exchange_token={}'.format(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET, short_lived_user_token)
    response = requests.get(url)
    return response.json()