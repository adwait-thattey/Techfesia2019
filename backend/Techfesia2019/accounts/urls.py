from django.urls import path, include

from . import views

app_name="accounts"

urlpatterns = [

    path('<str:username>/', include([

        path('email_confirmation', views.EmailConfirmed.as_view(), name="email_confirmed"),
        path('update_profile_pic', views.ProfilePictureUpdateView.as_view(), name="upload_profile_pic"),
        path('activate/<uidb64>/<token>', views.activate, name="activate_account")

    ])),
]