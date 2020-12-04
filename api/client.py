import urllib

import requests


class FaceBookHelperClient(object):
    BASE_URL = 'https://graph.facebook.com/v8.0'

    def __init__(self, user):
        facebook = user.social_media_handle.first()
        self.ACCESS_TOKEN = facebook.user_access_token
        self.PAGE_ID = facebook.page_id
        self.PAGE_ACCESS_TOKEN = facebook.page_access_token

    def make_api_request(self, url, method="GET"):
        if method == "GET":
            response = requests.get(url)
        else:
            response = requests.post(url)
        return response

    def get_page_info(self):
        url = '{}/{}?fields=name,phone,about,emails,website&access_token={}'.format(self.BASE_URL, self.PAGE_ID, self.ACCESS_TOKEN)
        result = self.make_api_request(url)
        return result

    def update_page_info(self, data):
        encoded_data = urllib.parse.urlencode(data)
        url = '{}/{}?{}&access_token={}'.format(self.BASE_URL, self.PAGE_ID, encoded_data, self.PAGE_ACCESS_TOKEN)
        result = self.make_api_request(url, method='POST')
        return result
