from django.urls import path
from .views import TeamInvitationListView


urlpatterns = [
    path('', TeamInvitationListView.as_view()),
]
