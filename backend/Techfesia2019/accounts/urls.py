from django.urls import path
from .views import UsersViewPost, UserDetail, UserState, ProfilePictureUpload, DisableUser
from .views import UserPasswordSetReset

urlpatterns = [
    path('', UsersViewPost.as_view(), name='users_list'),
    path('<str:username>/', UserDetail.as_view(), name='user_detail'),
    path('<str:username>/privileges/', UserState.as_view(), name='user_state'),
    path('<str:username>/picture/', ProfilePictureUpload.as_view(), name='profile_picture_upload'),
    path('<str:username>/disable/', DisableUser.as_view(), name='disable_user'),
    path('<str:username>/password/', UserPasswordSetReset.as_view(), name='disable_user'),

]

