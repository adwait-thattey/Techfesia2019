from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from registration import views

app_name="registration"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello', views.Hello.as_view(), name="hello"),
    path('firebase/token', views.FirebaseTokenObtainPairView.as_view(), name="firebase_auth_token"),
    path('firebase', views.FirebaseAuthenticationView.as_view(), name='firebase_auth'),
]