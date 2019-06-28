from django.urls import path
from .views import TeamInvitationDetailView


urlpatterns = [
    path('', TeamInvitationDetailView.as_view()),
]
