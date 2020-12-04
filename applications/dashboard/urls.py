from django.urls import path

from applications.dashboard import views

urlpatterns = [
    path('facebook/', views.SocialUserLoginAPI.as_view(), name='api-social-auth-register'),
    path('social-handles/', views.SocialMediaPageInfo.as_view(), name='social-handles'),
    path('update-social-handles/', views.UpdateSocialMediaPageInfo.as_view(), name='update-social-handles'),
]
