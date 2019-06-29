from django.urls import path
from .views import TeamDetailEditDeleteView, TeamListCreateView, TeamInvitationCreateView, TeamInvitationDeleteView

urlpatterns = [
    path('', TeamListCreateView.as_view(), name='teams_list'),
    path('<str:public_id>/', TeamDetailEditDeleteView.as_view(), name='team_details'),
    path('<str:public_id>/invitations/', TeamInvitationCreateView.as_view(), name='create_invitation'),
    path('<str:public_id>/invitations/<str:username>/', TeamInvitationDeleteView.as_view(), name='create_invitation'),
]
