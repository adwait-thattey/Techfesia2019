from django.urls import path
from .views import TeamInvitationListView, TeamInvitationDetailView, TeamInvitationAcceptView, TeamInvitationRejectView


urlpatterns = [
    path('', TeamInvitationListView.as_view()),
    path('<str:team_public_id>', TeamInvitationDetailView.as_view()),
    path('<str:team_public_id>/accept/', TeamInvitationAcceptView.as_view()),
    path('<str:team_public_id>/reject/', TeamInvitationRejectView.as_view()),
]
