import facebook
import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.client import FaceBookHelperClient
from api.helpers import get_long_lived_user_token
from applications.dashboard.models import SocialMediaAccessToken
from applications.dashboard.serializers import SocialSerializer, UpdatePageInfoSerializer


class SocialUserLoginAPI(APIView):

    def post(self, request):
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            try:
                graph = facebook.GraphAPI(access_token=serializer.validated_data['access_token'])
                user_details = graph.get_object(id='me', fields='first_name,last_name, email')
                if User.objects.filter(email__iexact=user_details.get('email')).exists():
                    user = User.objects.get(email__iexact=user_details.get('email'))
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'message': 'success', 'key': token.key})
                else:
                    password = User.objects.make_random_password()
                    data = {'email': user_details.get('email'), 'username': user_details.get('email'),
                            'first_name': user_details.get('first_name'),
                            'last_name': user_details.get('last_name'),
                            'password': password,
                            'is_active': True}
                    user = User.objects.create(**data)
                    token, _ = Token.objects.get_or_create(user=user)
                    self.check_for_social_handle(user_details, serializer.validated_data['access_token'], user)
                    return Response({'message': 'success', 'key': token.key})
            except Exception as e:
                return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)

    def check_for_social_handle(self, data, token, user):
        try:
            user_token = get_long_lived_user_token(token)['access_token']
            url = 'https://graph.facebook.com/{}/accounts?fields=name,access_token&access_token={}'.format(data['id'], token)
            response = requests.get(url)
            result = response.json()
            if response.status_code == 200 and len(result['data']):
                social_token = {'name': 'facebook', 'page_id': result['data'][0]['id'],
                                'user_access_token': user_token,
                                'user': user, 'page_access_token': result['data'][0]['access_token']}
                SocialMediaAccessToken.objects.create(**social_token)
        except KeyError as e:
            print(e)


class SocialMediaPageInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.social_media_handle.exists():
            facebook_client = FaceBookHelperClient(request.user)
            result = facebook_client.get_page_info()
            if result.status_code == 200:
                return Response({'message': [result.json()]}, status=200)
        return Response({'message': "No page associated with this user"}, status=status.HTTP_403_FORBIDDEN)


class UpdateSocialMediaPageInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        cleaned_data = {field: value for field, value in request.data.items() if value}
        serializer = UpdatePageInfoSerializer(data=cleaned_data)

        if serializer.is_valid() and request.user.social_media_handle.exists():
            facebook_client = FaceBookHelperClient(request.user)
            response = facebook_client.update_page_info(serializer.validated_data)
            if response.status_code == 200:
                return Response({'message': response.json()})
            else:
                return Response({'message': response.json()['error']}, status=response.status_code)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
