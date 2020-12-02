from django.urls import path

from applications.dashboard import views

urlpatterns = [
    path('facebook/', views.SocialUserLoginAPI.as_view(), name='api-social-auth-register'),
    path('social-handles/', views.SocialMediaPage.as_view(), name='social-handles'),
]
