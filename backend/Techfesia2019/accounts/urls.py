from django.urls import path

from . import views

app_name="accounts"

urlpatterns = [
    path('<str:username>/email_confirmation', views.EmailConfirmed.as_view(), name="email_confirmed"),
    path('<str:username>/activate/<uidb64>/<token>', views.activate, name="activate_account" )
]