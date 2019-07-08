from django.urls import path
from .views import TeamDetailEditDeleteView, TeamListCreateView, TeamInvitationCreateView, TeamInvitationDeleteView
from .views import TeamMemberDeleteView

urlpatterns = [
    path('', TeamListCreateView.as_view(), name='teams_list_create'),
    path('<str:public_id>/', TeamDetailEditDeleteView.as_view(), name='team_details'),
    path('<str:public_id>/invitations/', TeamInvitationCreateView.as_view(), name='create_invitation'),
    path('<str:public_id>/delete/<str:username>/', TeamMemberDeleteView.as_view(), name='delete_member'),
    path('<str:public_id>/invitations/<str:username>/', TeamInvitationDeleteView.as_view(), name='delete_invitation'),
]
