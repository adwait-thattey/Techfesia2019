from django.urls import path
from .views import TeamInvitationListView, TeamInvitationDetailView, TeamInvitationAcceptView, TeamInvitationRejectView


urlpatterns = [
    path('', TeamInvitationListView.as_view(), name='list_invitation'),
    path('<str:team_public_id>', TeamInvitationDetailView.as_view(), name='invitation_detail'),
    path('<str:team_public_id>/accept/', TeamInvitationAcceptView.as_view(), name='accept_invitation'),
    path('<str:team_public_id>/reject/', TeamInvitationRejectView.as_view(), name='reject_invitation'),
]
