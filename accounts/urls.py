from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, UserLogoutAPIView
# from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='user-signup'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    # path('login/', auth_views.obtain_auth_token, name='api-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
]
